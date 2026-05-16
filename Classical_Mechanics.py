import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==============================
# FUTURISTIC CLASSICAL MECHANICS LAB
# ==============================

plt.style.use("dark_background")

class ClassicalMechanicsSimulator:

    def __init__(self):

        self.fig, self.axes = plt.subplots(2, 2, figsize=(16, 10))
        self.fig.patch.set_facecolor("#0a0a0a")

        self.fig.suptitle(
            "⚛ Classical Mechanics Simulations ⚛",
            fontsize=20,
            color="cyan",
            fontweight="bold"
        )

        # Colors
        self.colors = {
            "cyan": "#00ffff",
            "orange": "#ff9900",
            "green": "#00ff88",
            "magenta": "#ff00ff",
            "red": "#ff4444",
            "blue": "#4488ff"
        }

        # Styling axes
        for row in self.axes:
            for ax in row:
                ax.set_facecolor("#111111")
                ax.grid(True, alpha=0.3, linestyle="--")

        # Parameters
        self.velocity = 50
        self.theta0 = np.pi / 4

    # ==================================
    # PENDULUM MOTION
    # ==================================
    def pendulum_motion(self):

        ax = self.axes[0, 0]

        g = 9.81
        L = 1.0

        t = np.linspace(0, 10, 1000)

        omega = np.sqrt(g / L)

        theta = self.theta0 * np.cos(omega * t)

        ax.plot(
            t,
            theta,
            color=self.colors["cyan"],
            linewidth=2.5
        )

        ax.fill_between(
            t,
            theta,
            color=self.colors["cyan"],
            alpha=0.15
        )

        ax.set_title(
            "Pendulum Angle vs Time",
            color="white",
            fontsize=14
        )

        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Angle (rad)")

    # ==================================
    # PROJECTILE MOTION
    # ==================================
    def projectile_motion(self):

        ax = self.axes[0, 1]

        v0 = self.velocity
        angles = [30, 45, 60]
        g = 9.81

        colors = [
            self.colors["blue"],
            self.colors["orange"],
            self.colors["green"]
        ]

        for angle, c in zip(angles, colors):

            theta = np.radians(angle)

            t_flight = 2 * v0 * np.sin(theta) / g

            t = np.linspace(0, t_flight, 200)

            x = v0 * np.cos(theta) * t
            y = v0 * np.sin(theta) * t - 0.5 * g * t**2

            ax.plot(
                x,
                y,
                linewidth=3,
                color=c,
                label=f"{angle}°"
            )

            ax.scatter(
                x[-1],
                y[-1],
                s=80,
                color=c
            )

        ax.set_title(
            "Projectile Motion",
            color="white",
            fontsize=14
        )

        ax.set_xlabel("Distance (m)")
        ax.set_ylabel("Height (m)")
        ax.legend()

    # ==================================
    # DAMPED HARMONIC OSCILLATOR
    # ==================================
    def harmonic_oscillator(self):

        ax = self.axes[1, 0]

        t = np.linspace(0, 10, 1000)

        gamma_values = [0, 0.5, 1, 2]

        colors = [
            self.colors["blue"],
            self.colors["orange"],
            self.colors["green"],
            self.colors["red"]
        ]

        for gamma, c in zip(gamma_values, colors):

            if gamma == 0:

                y = np.cos(t)
                label = "Undamped (γ=0)"

            elif gamma < 1:

                omega_d = np.sqrt(1 - gamma**2)

                y = np.exp(-gamma * t) * np.cos(omega_d * t)

                label = f"Underdamped (γ={gamma})"

            elif gamma == 1:

                y = (1 + t) * np.exp(-t)

                label = "Critically Damped (γ=1)"

            else:

                y = (
                    0.5
                    * np.exp(-t)
                    * (
                        np.exp(t * np.sqrt(gamma**2 - 1))
                        + np.exp(-t * np.sqrt(gamma**2 - 1))
                    )
                )

                label = f"Overdamped (γ={gamma})"

            ax.plot(
                t,
                y,
                linewidth=2.5,
                color=c,
                label=label
            )

        ax.set_title(
            "Damped Harmonic Oscillator",
            color="white",
            fontsize=14
        )

        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Displacement (m)")
        ax.legend()

    # ==================================
    # ENERGY CONSERVATION
    # ==================================
    def energy_conservation(self):

        ax = self.axes[1, 1]

        g = 9.81
        L = 1.0

        theta0 = np.pi / 3

        t = np.linspace(0, 4 * np.pi / np.sqrt(g / L), 1000)

        theta = theta0 * np.cos(np.sqrt(g / L) * t)

        V = 0.5 * g * L * theta**2

        K = (
            0.5
            * L**2
            * (theta0 * np.sqrt(g / L))**2
            * np.sin(np.sqrt(g / L) * t)**2
        )

        E_total = V + K

        ax.plot(
            t,
            V,
            color=self.colors["red"],
            linewidth=2.5,
            label="Potential Energy"
        )

        ax.plot(
            t,
            K,
            color=self.colors["blue"],
            linewidth=2.5,
            label="Kinetic Energy"
        )

        ax.plot(
            t,
            E_total,
            "--",
            color="white",
            linewidth=2.5,
            label="Total Energy"
        )

        ax.fill_between(
            t,
            V,
            color=self.colors["red"],
            alpha=0.1
        )

        ax.fill_between(
            t,
            K,
            color=self.colors["blue"],
            alpha=0.1
        )

        ax.set_title(
            "Energy Conservation",
            color="white",
            fontsize=14
        )

        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Energy")
        ax.legend()

    # ==================================
    # FIXED ANIMATED PENDULUM
    # ==================================
    def pendulum_animation(self):

        fig_anim, ax_anim = plt.subplots(figsize=(5, 5))

        fig_anim.patch.set_facecolor("#0a0a0a")
        ax_anim.set_facecolor("#111111")

        ax_anim.set_xlim(-1.2, 1.2)
        ax_anim.set_ylim(-1.2, 0.2)

        ax_anim.set_title(
            "Animated Pendulum",
            color="cyan",
            fontsize=16
        )

        ax_anim.grid(True, alpha=0.3, linestyle="--")

        line, = ax_anim.plot(
            [],
            [],
            "o-",
            lw=3,
            color="cyan",
            markersize=12
        )

        g = 9.81
        L = 1

        t = np.linspace(0, 10, 500)

        theta = self.theta0 * np.cos(np.sqrt(g / L) * t)

        x = L * np.sin(theta)
        y = -L * np.cos(theta)

        def init():

            line.set_data([], [])

            return line,

        def update(frame):

            line.set_data(
                [0, x[frame]],
                [0, y[frame]]
            )

            return line,

        # IMPORTANT FIX
        self.ani = FuncAnimation(
            fig_anim,
            update,
            frames=len(t),
            init_func=init,
            interval=20,
            blit=True,
            repeat=True
        )

        return self.ani

    # ==================================
    # RUN EVERYTHING
    # ==================================
    def run_simulation(self):

        self.pendulum_motion()

        self.projectile_motion()

        self.harmonic_oscillator()

        self.energy_conservation()

        # Animated pendulum
        self.pendulum_animation()

        # Physics info
        self.fig.text(
            0.02,
            0.02,
            "Simulations Included: Pendulum | Projectile | Oscillator | Energy Conservation",
            fontsize=10,
            color="white"
        )

        plt.tight_layout()

        plt.savefig(
            "classical_mechanics_lab.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.show()


# ==============================
# RUN PROGRAM
# ==============================

simulator = ClassicalMechanicsSimulator()
simulator.run_simulation()