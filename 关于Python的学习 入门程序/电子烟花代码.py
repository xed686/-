import pygame
import random
import math
import sys

# 初始化pygame，解决PyCharm中可能的初始化警告
pygame.init()
pygame.mixer.quit()  # 关闭音频（避免无音频设备的报错）

# 适配PyCharm的窗口设置（可选：注释掉下面3行，取消注释第14行可改为全屏）
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # 全屏模式（需ESC退出）

pygame.display.set_caption("PyCharm 烟花特效")

# 颜色定义
BLACK = (0, 0, 0)

# 控制帧率（保证动画流畅）
clock = pygame.time.Clock()

# 粒子类：烟花爆炸后的粒子效果
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.speed = random.uniform(1, 5)  # 粒子扩散速度
        self.angle = random.uniform(0, math.pi * 2)  # 随机扩散角度
        self.gravity = 0.05  # 重力加速度（模拟下落）
        self.vx = math.cos(self.angle) * self.speed  # x方向速度
        self.vy = math.sin(self.angle) * self.speed  # y方向速度
        self.alpha = 255  # 粒子透明度
        self.decay = random.uniform(3, 5)  # 透明度衰减速度
        self.color = color  # 粒子颜色

    def update(self):
        """更新粒子位置和透明度"""
        self.vy += self.gravity  # 重力影响，y方向速度增加
        self.x += self.vx
        self.y += self.vy
        self.alpha -= self.decay  # 透明度降低
        # 空气阻力：速度逐渐减慢
        self.vx *= 0.98
        self.vy *= 0.98

    def draw(self):
        """绘制带透明度的粒子（适配PyCharm的渲染）"""
        if self.alpha > 0:
            # 创建透明表面绘制粒子，避免直接绘制导致的透明度异常
            temp_surf = pygame.Surface((4, 4), pygame.SRCALPHA)
            color_with_alpha = (*self.color, int(self.alpha))
            pygame.draw.circle(temp_surf, color_with_alpha, (2, 2), 2)
            screen.blit(temp_surf, (self.x, self.y))

# 烟花类：控制升空和爆炸
class Firework:
    def __init__(self, x, y):
        self.x = x  # 烟花起始x坐标（鼠标点击位置）
        self.y = SCREEN_HEIGHT  # 烟花从屏幕底部升空
        self.target_y = y  # 爆炸目标y坐标（鼠标点击位置）
        self.speed = random.uniform(8, 12)  # 升空速度
        # 随机鲜艳颜色
        self.color = (
            random.randint(180, 255),
            random.randint(180, 255),
            random.randint(180, 255)
        )
        self.exploded = False  # 是否爆炸
        self.particles = []  # 爆炸后的粒子列表

    def update(self):
        """更新烟花状态"""
        if not self.exploded:
            # 向目标位置升空
            self.y -= self.speed
            # 到达目标位置触发爆炸
            if self.y <= self.target_y:
                self.explode()
                self.exploded = True
        else:
            # 更新所有粒子，移除透明度为0的粒子
            for particle in self.particles[:]:
                particle.update()
                if particle.alpha <= 0:
                    self.particles.remove(particle)

    def explode(self):
        """生成爆炸粒子（100-200个）"""
        particle_count = random.randint(100, 200)
        for _ in range(particle_count):
            self.particles.append(Particle(self.x, self.y, self.color))

    def draw(self):
        """绘制烟花（升空阶段/爆炸阶段）"""
        if not self.exploded:
            # 升空阶段：绘制小光点
            pygame.draw.circle(screen, self.color, (self.x, self.y), 3)
        else:
            # 爆炸阶段：绘制所有粒子
            for particle in self.particles:
                particle.draw()

# 主程序逻辑（PyCharm中运行的核心）
def main():
    fireworks = []  # 存储所有烟花实例
    running = True

    while running:
        clock.tick(60)  # 固定60帧
        screen.fill(BLACK)  # 黑色背景

        # 事件处理（PyCharm中正常响应鼠标/键盘）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC键退出
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标点击发射烟花
                click_x, click_y = pygame.mouse.get_pos()
                fireworks.append(Firework(click_x, click_y))

        # 更新并绘制所有烟花
        for firework in fireworks[:]:
            firework.update()
            firework.draw()
            # 移除爆炸后无粒子的烟花（释放内存）
            if firework.exploded and len(firework.particles) == 0:
                fireworks.remove(firework)

        pygame.display.flip()  # 更新屏幕显示

    # 退出清理
    pygame.quit()
    sys.exit()

# PyCharm中直接运行的入口
if __name__ == "__main__":
    main()