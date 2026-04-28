import numpy as np
import matplotlib.pyplot as plt


class Drunkard2D:
    def __init__(self, num_drunkards, init_pos=None, is_limited=False, bounds=None):
        self._n_d = num_drunkards
        self._is_limited = is_limited
        self._bounds = bounds if bounds else [-100, -100, 100, 100]

        if init_pos is not None:
            self._pos = np.array(init_pos, dtype=float)
        else:
            # Початкова позиція в центрі або в (0,0)
            self._pos = np.zeros((2, self._n_d))
            if self._is_limited:
                xmin, ymin, xmax, ymax = self._bounds
                self._pos[0, :] = (xmin + xmax) / 2
                self._pos[1, :] = (ymin + ymax) / 2

        # Можливі напрямки: вліво, вниз, вправо, вгору
        self._dirs = np.array([[-1, 0], [0, -1], [1, 0], [0, 1]]).T

    def _push_into_bounds(self):
        """Відбиття точок від стінок (обмеження області)."""
        xmin, ymin, xmax, ymax = self._bounds
        # Використовуємо np.clip для ефективного обмеження координат
        self._pos[0] = np.clip(self._pos[0], xmin, xmax)
        self._pos[1] = np.clip(self._pos[1], ymin, ymax)

    def step(self):
        """Один випадковий крок для всіх точок одночасно."""
        # Новий генератор випадкових чисел (рекомендовано в NumPy)
        rng = np.random.default_rng()
        ids = rng.integers(0, 4, self._n_d)

        dxy = self._dirs[:, ids]
        self._pos += dxy

        if self._is_limited:
            self._push_into_bounds()

    def msteps(self, m):
        for _ in range(m):
            self.step()

    def show(self):
        plt.figure(figsize=(8, 8))
        plt.scatter(self._pos[0], self._pos[1], s=10, alpha=0.5, c='royalblue')
        xmin, ymin, xmax, ymax = self._bounds
        plt.xlim(xmin - 10, xmax + 10)
        plt.ylim(ymin - 10, ymax + 10)
        plt.title(f"Random Walk: {self._n_d} particles")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()


if __name__ == '__main__':
    # Створюємо обмежену область (газ у контейнері)
    ds = Drunkard2D(1000, is_limited=True, bounds=[-50, -50, 50, 50])
    ds.msteps(500)
    ds.show()