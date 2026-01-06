import pygame

Tile_color = {
    0 : (0, 0, 0),
    1 : (0, 255, 0),
}

class Renderer:
    def __init__(self, env, cell=64):
        pygame.init()
        self.env = env
        self.cell = cell

        self.width = env.width*cell
        self.height = env.height*cell

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.background = pygame.Surface((self.width, self.height))
        self.render_bg()

        self.sprite = env.sprite

    def render_bg(self):
        for y in range(self.env.width):
            for x in range(self.env.height):
                tile = self.env.bg_color[x, y]
                if (x != self.env.sprite[0] or y != self.env.sprite[1]) and (x != self.env.target[0] or y != self.env.target[1]):
                    colors = Tile_color[tile]
                elif x == self.env.sprite[0] and y == self.env.sprite[1]:
                    colors = (255, 0, 0)
                else:
                    colors = (0, 0, 255)
                rect = pygame.Rect(y*self.cell, x*self.cell, self.cell, self.cell)
                pygame.draw.rect(self.background, colors, rect)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
