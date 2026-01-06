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

        self.sprite = env.sprite

        pygame.font.init()
        self.font=pygame.font.SysFont('Comic Sans MS', 30)

    def render_bg(self, counter):
        for y in range(self.env.width):
            for x in range(self.env.height):
                tile = self.env.bg_color[x, y]
                colors = Tile_color[tile]
                if x == self.env.sprite[0] and y == self.env.sprite[1]:
                    colors = (255, 0, 0)
                elif x == self.env.target[0] and y == self.env.target[1]:
                    colors = (0, 0, 255)
                else:
                    colors = Tile_color[tile]
                rect = pygame.Rect(y*self.cell, x*self.cell, self.cell, self.cell)
                pygame.draw.rect(self.background, colors, rect)
        text_surface = self.font.render(str(counter), True, (255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(text_surface, (590, 10))
        pygame.display.flip()
