"""Independent check of the central claim in openscientist.md.

Question: if only free cortisol is cleared (restrictive clearance), does removing
CBG lower the free-cortisol exposure or the free-cortisol peak of a stress episode?

One well-mixed plasma compartment. Total T = F + CBG-bound + albumin-bound, with
instantaneous equilibrium: bound_CBG = Bmax*F/(Kd+F), bound_alb = k_alb*F.
dT/dt = S(t) - CL*F. Written from the description in the report, not from the
provider's code, which was not delivered. Parameter values are round numbers in
the physiological range and are swept; they are assumptions, not measurements.

Run: python openscientist-assessment-by-claude-code-replication.py
"""
import itertools
import math


def free_from_total(total, bmax, kd, k_alb):
    # solve T = F*(1+k_alb) + bmax*F/(kd+F) for F >= 0
    a = 1 + k_alb
    b = a * kd + bmax - total
    c = -total * kd
    return (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)


def run(bmax, kd=30.0, k_alb=1.7, cl=1.0, basal=10.0, stress_mult=5.0, dur=1.0):
    def secretion(t):
        return basal * (stress_mult if 2.0 <= t < 2.0 + dur else 1.0)

    f0 = basal / cl
    t0 = f0 * (1 + k_alb) + bmax * f0 / (kd + f0)

    def rhs(t, total):
        return secretion(t) - cl * free_from_total(total, bmax, kd, k_alb)

    # fixed-step fourth-order Runge-Kutta, 36 h, step 0.002 h
    dt, total, t = 0.002, t0, 0.0
    free_auc, free_peak, total_peak = 0.0, f0, t0
    prev_free = f0
    for _ in range(int(36 / dt)):
        k1 = rhs(t, total)
        k2 = rhs(t + dt / 2, total + dt * k1 / 2)
        k3 = rhs(t + dt / 2, total + dt * k2 / 2)
        k4 = rhs(t + dt, total + dt * k3)
        total += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += dt
        free = free_from_total(total, bmax, kd, k_alb)
        free_auc += dt * (free + prev_free) / 2
        prev_free = free
        free_peak = max(free_peak, free)
        total_peak = max(total_peak, total)
    return dict(rest_free=f0, rest_total=t0, free_auc=free_auc,
                free_peak=free_peak, total_peak=total_peak)


print("kd\tk_alb\tmult\tdur_h\trest_total_ratio\tfree_auc_ratio\tfree_peak_ratio\ttotal_peak_ratio")
for kd, k_alb, mult, dur in itertools.product((15.0, 30.0, 60.0), (1.0, 1.7), (3.0, 5.0, 10.0), (0.5, 1.0, 3.0)):
    wt = run(700.0, kd, k_alb, stress_mult=mult, dur=dur)
    null = run(0.0, kd, k_alb, stress_mult=mult, dur=dur)
    print(f"{kd}\t{k_alb}\t{mult}\t{dur}\t{null['rest_total']/wt['rest_total']:.3f}\t"
          f"{null['free_auc']/wt['free_auc']:.4f}\t{null['free_peak']/wt['free_peak']:.3f}\t"
          f"{null['total_peak']/wt['total_peak']:.3f}")
