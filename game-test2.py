import pygame
import sys
import os
import random
import math

# Sound settings
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=256)

# Game settings
TILESIZE = 50
WIDTH = 19 * TILESIZE
HEIGHT = 11 * TILESIZE
FPS = 70

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 120, 255)
GREEN = (0, 255, 0)
PURPLE = (180, 0, 255)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

# Game levels
levels = [
    [
        "WWWWWWWWWWWWWWWWWW",
        "W......R.........WW",
        "W..R.....W......WWW",
        "W........W.R.E...WW",
        "W..P..........WW.WW",
        "W.......W...R....WW",
        "W.....W.........WWW",
        "W......W..R......WW",
        "W...R..W...R.....WW",
        "W.....W..R.......WW",
        "WWWWWWWWWWWWWWWWWW"  
    ],
    [
        "WWWWWWWWWWWWWWWWWW",
        "WP...R...W......WW",
        "W..WW.......W...WWW",
        "W.......W......WWWW",
        "W..........R....WWW",
        "W.......W...R....WW",
        "W.....W.....R....WWW",
        "W......W..R......WW",
        "W...R..W...R.....WW",
        "W..RW...W....RR..EW",
        "WWWWWWWWWWWWWWWWWW"
    ],
    [
        "WWWWWWWWWWWWWWWWWWW",
        "WP..W...R....W....WWW",
        "W..W.......WW...WWWWW",
        "W..W..RWR..........WW",
        "W...R....W...E...W.WW",
        "W.....W.....R....WWWW",
        "W.......W...R....WWWW",
        "W.....W.........WWWWW",
        "W......W..R......WWWW",
        "W...R..W...R....WWWW",
        "WWWWWWWWWWWWWWWWWWWW"
    ],
    [
        "WWWWWWWWWWWWWWWWWWW",
        "WP...W...W......WWW",
        "W..WW....R...W.E.WW",
        "W....R...W.....W.WW",
        "W..R...W.....R....W",
        "W..E...R...WW.....W",
        "W.......W...R...WWW",
        "W.....W..........WW",
        "W......W..R.....WWW",
        "W.....W..RWR.....WW",
        "WWWWWWWWWWWWWWWWWWWW"
    ],
    [
        "WWWWWWWWWWWWWWWWWWW",
        "W.P..W......WWR..WW",
        "W..W...R....W....WW",
        "W..W.......WW...WWW",
        "W...R....W.....WWWW",
        "W.....W.....R...WWW",
        "W....R.WR........WW",
        "W.......W...R...WWW",
        "W....W..W...E..WWWW",
        "W......W..R.....WWW",
        "WWWWWWWWWWWWWWWWWWW"
    ],
    [
        "WWWWWWWWWWWWWWWWWWWW",
        "W...W.....P.....WWWW",
        "W..W......WW...WWWWW",
        "W..W.......R....WWWW",
        "W...R....W.....WWWWW",
        "W.....W.....R...WWWW",
        "W.....WR........WWWW",
        "W.......W...R...WWWW",
        "W...R.W....E....WWWW",
        "W..R...W..R.....WWWW",
        "WWWWWWWWWWWWWWWWWWWW"
    ],
    [
        "WWWWWWWWWWWWWWWWWWWW",
        "W...WW...R.........W",
        "W........R...W.....W",
        "WW...R....W..R.....W",
        "W.....R....EW......W",
        "W........W.......WW.",
        "W...P....W....R....W",
        "W..R.....WW......R.W",
        "W......RW.......R..W",
        "W.....RW..........RW",
        "WWWWWWWWWWWWWWWWWWWW"
    ],
    [
        "WWWWWWWWWWWWWWWWWWWW",
        "W...P....W.....W...W",
        "W........R...W.....W",
        "WW...R.....W.R.....W",
        "W.....R....W......W",
        "W........W....E...WW.",
        "W...W....W....R....W",
        "W..R.....WW......R.W",
        "W....W..RW.......R..W",
        "W.....WR.......W...RW",
        "W....W.R....W.......W",
        "WWWWWWWWWWWWWWWWWWWW"
    ],
    [
        "WWWWWWWWWWWWWWWWWWWW",
        "W...P....W.....W...W",
        "W........R...W.....W",
        "WW...R.....W.R.....W",
        "W.....R....W......W",
        "W........W.......WW.",
        "W...W....W....R....W",
        "W..R.....WW......R.W",
        "W....W..RW.......R..W",
        "W.....WR.......W...RW",
        "W....W.R....W..E....W",
        "WWWWWWWWWWWWWWWWWWWW"
    ],
    # Final level with boss
    [
        "WWWWWWWWWWWWWWWWWWWWWWW",
        "WWWWW..............WWWW",
        "WWW...W.W..W..W.W...WWW",
        "WW..W.........P...W..WW",
        "W....W..W..W..W..W....W",
        "W..W...............W..W",
        "W...........E........WW",
        "W..W.W.W..W..W..W.W..W",
        "WW...................WW",
        "WWW.W.W..W..W..W.W.WWWW",
        "WWWWW..............WWW",
        "WWWWWWWWWWWWWWWWWWWWWWW"
    ],
]

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Escape from Laboratory")
        self.clock = pygame.time.Clock()
        self.running = True

        self.lives = 15
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.small_font = pygame.font.SysFont(None, 24)
        self.big_font = pygame.font.SysFont(None, 72)

        # Power-up system
        self.power_up_unlocked = False  # Level 1: Robot transformation
        self.power_up_active = False  # Is power-up active?
        self.power_up_duration = 30  # Power-up duration in seconds
        self.power_up_timer = 0  # Power-up timer
        self.power_up_used_this_level = False  # Used this level?
        self.power_up_cooldown = 0  # Cooldown between uses
        
        # Shooting system (unlocked at 3000 points)
        self.shooting_unlocked = False  # Level 2: Shooting ability
        self.bullets_remaining = 0  # Bullets available
        self.max_bullets = 15  # Maximum bullets per level
        self.bullets_used_this_level = 0  # Bullets used this level
        
        # Levels
        self.level_index = 0
        self.map_data = levels[self.level_index]
        
        # Boss state
        self.boss_defeated = False

        # Load images - SMALLER CHARACTER SIZES
        self.floor_img = pygame.transform.scale(pygame.image.load("lab_floor.png"), (TILESIZE, TILESIZE))
        self.wall_img = pygame.transform.scale(pygame.image.load("metal_wall.png"), (TILESIZE, TILESIZE))
        
        # SMALLER PLAYER IMAGE: 32x32 instead of 40x40
        self.player_img = pygame.transform.scale(pygame.image.load("scientist_player.png"), (32, 32))
        
        self.exit_img = pygame.transform.scale(pygame.image.load("exit_door.png"), (TILESIZE, TILESIZE))
        
        # SMALLER ROBOT IMAGE: 32x32 instead of 40x40
        self.robot_img = pygame.transform.scale(pygame.image.load("robot_lab.png"), (32, 32))
        
        self.background_img = pygame.transform.scale(pygame.image.load("lab_background.png"), (WIDTH, HEIGHT))
        
        # Boss image - slightly smaller
        try:
            self.boss_img = pygame.transform.scale(pygame.image.load("boss.png"), (TILESIZE * 1.6, TILESIZE * 1.6))
        except:
            self.boss_img = None
        
        # Robot player image - SMALLER SIZE: 32x32
        try:
            # Load and resize robot image
            original_robot = pygame.image.load("robot_lab.png")
            # First resize to 32x32
            small_robot = pygame.transform.scale(original_robot, (32, 32))
            # Then apply color tint
            self.robot_player_img = self.create_colored_robot_image(small_robot)
        except:
            # If no robot image exists, create a blue robot
            self.robot_player_img = pygame.Surface((32, 32))
            self.robot_player_img.fill((0, 120, 255))
            pygame.draw.rect(self.robot_player_img, (0, 80, 200), (4, 4, 24, 24))
            pygame.draw.circle(self.robot_player_img, YELLOW, (16, 16), 6)

        # Load sounds
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.sound_win = pygame.mixer.Sound("win.wav")
        self.sound_lose = pygame.mixer.Sound("lose.wav")
        self.sound_gameover = pygame.mixer.Sound("game over.mp3")
        self.sound_boss_hit = pygame.mixer.Sound("boss_hit.wav") if os.path.exists("boss_hit.wav") else None
        self.sound_power_up = pygame.mixer.Sound("power_up.wav") if os.path.exists("power_up.wav") else None
        self.sound_shoot = pygame.mixer.Sound("shoot.wav") if os.path.exists("shoot.wav") else None
        self.sound_boss_defeat = pygame.mixer.Sound("boss_defeat.wav") if os.path.exists("boss_defeat.wav") else None

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.robots = pygame.sprite.Group()
        self.boss = None
        self.boss_attacks = pygame.sprite.Group()

        self.load_map()
    
    def create_colored_robot_image(self, robot_image):
        """Create a colored version of the robot image to differentiate from enemies"""
        try:
            # Create a blue tint overlay for 32x32 image
            overlay = pygame.Surface((32, 32), pygame.SRCALPHA)
            overlay.fill((0, 100, 255, 64))  # Semi-transparent blue
            
            # Create final image with blue tint
            final_img = pygame.Surface((32, 32), pygame.SRCALPHA)
            final_img.blit(robot_image, (0, 0))
            final_img.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
            
            # Add a yellow glow effect
            pygame.draw.circle(final_img, (255, 255, 100, 128), 
                             (16, 16), 10, 2)  # Smaller glow for 32x32 image
            
            return final_img
        except:
            # Fallback if image processing fails
            img = pygame.Surface((32, 32))
            img.fill((0, 120, 255))
            pygame.draw.rect(img, (0, 80, 200), (4, 4, 24, 24))
            pygame.draw.circle(img, YELLOW, (16, 16), 6)
            return img

    def load_map(self):
        # Reset level-specific power-up states
        self.power_up_used_this_level = False
        self.power_up_active = False
        self.bullets_used_this_level = 0
        
        # Reset bullets for this level
        if self.shooting_unlocked:
            self.bullets_remaining = self.max_bullets
        
        # UNLIMITED BULLETS IN FINAL LEVEL
        if self.level_index == len(levels) - 1:
            self.bullets_remaining = 999  # Unlimited bullets indicator
        
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                pos = (x * TILESIZE, y * TILESIZE)
                Floor(pos, self.floor_img, self.all_sprites)
                if tile == "W":
                    Wall(pos, self.wall_img, self.all_sprites, self.walls)
                elif tile == "P":
                    # Player position adjusted for smaller sprite
                    adjusted_pos = (pos[0] + 4, pos[1] + 4)  # Center 32x32 in 40x40 tile
                    self.player = Player(adjusted_pos, self.player_img, self.all_sprites, self.walls, self, self.robot_player_img)
                elif tile == "R":
                    # Robot position adjusted for smaller sprite
                    adjusted_pos = (pos[0] + 4, pos[1] + 4)  # Center 32x32 in 40x40 tile
                    Robot(adjusted_pos, self.robot_img, self.all_sprites, self.robots, self.walls)
                elif tile == "E":
                    self.exit_rect = self.exit_img.get_rect(topleft=pos)
                    self.exit_pos = pos
                elif tile == "B":
                    self.boss = Boss(pos, self.boss_img, self.all_sprites, self.walls, self.player, self.boss_attacks, self)
        
        # If final level and no boss, add one
        if self.level_index == len(levels) - 1 and self.boss is None:
            center_x = len(self.map_data[0]) // 2 * TILESIZE
            center_y = len(self.map_data) // 2 * TILESIZE
            boss_pos = (center_x, center_y)
            self.boss = Boss(boss_pos, self.boss_img, self.all_sprites, self.walls, self.player, self.boss_attacks, self)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                # Shooting system with separate keys
                if event.key == pygame.K_SPACE and not self.power_up_active:
                    # UNLIMITED BULLETS IN FINAL LEVEL - always allow shooting
                    if self.level_index == len(levels) - 1:
                        self.player.shoot("up")
                        if self.sound_shoot:
                            self.sound_shoot.play()
                    else:
                        # Normal shooting logic for other levels
                        if self.shooting_unlocked:
                            if self.bullets_remaining > 0:
                                self.player.shoot("up")
                                self.bullets_remaining -= 1
                                self.bullets_used_this_level += 1
                                if self.sound_shoot:
                                    self.sound_shoot.play()
                        elif not self.power_up_active:
                            # Unlimited shooting if not unlocked yet
                            self.player.shoot("up")
                
                # Shooting keys for different directions
                shooting_keys = {
                    pygame.K_w: "up",      # W for up
                    pygame.K_s: "down",    # S for down
                    pygame.K_a: "left",    # A for left
                    pygame.K_d: "right",   # D for right
                    pygame.K_q: "up-left",     # Q for up-left
                    pygame.K_e: "up-right",    # E for up-right
                    pygame.K_z: "down-left",   # Z for down-left
                    pygame.K_c: "down-right",  # C for down-right
                }
                
                for key, direction in shooting_keys.items():
                    if event.key == key and not self.power_up_active:
                        # UNLIMITED BULLETS IN FINAL LEVEL
                        if self.level_index == len(levels) - 1:
                            self.player.shoot(direction)
                            if self.sound_shoot:
                                self.sound_shoot.play()
                        else:
                            # Normal shooting logic for other levels
                            if self.shooting_unlocked:
                                if self.bullets_remaining > 0:
                                    self.player.shoot(direction)
                                    self.bullets_remaining -= 1
                                    self.bullets_used_this_level += 1
                                    if self.sound_shoot:
                                        self.sound_shoot.play()
                            elif not self.power_up_active:
                                # Unlimited shooting if not unlocked
                                self.player.shoot(direction)
                
                # Activate robot power-up with F key
                if event.key == pygame.K_f and self.power_up_unlocked and not self.power_up_active and not self.power_up_used_this_level and self.power_up_cooldown <= 0:
                    self.activate_power_up()

    def activate_power_up(self):
        """Activate robot transformation power-up"""
        self.power_up_active = True
        self.power_up_used_this_level = True
        self.power_up_timer = self.power_up_duration * FPS
        
        # Change player image to robot form (using robot_lab.png)
        self.player.activate_robot_form()
        
        # Play sound
        if self.sound_power_up:
            self.sound_power_up.play()
        
        print(f"Robot transformation activated! {self.power_up_duration} seconds remaining!")

    def deactivate_power_up(self):
        """Deactivate robot transformation power-up"""
        self.power_up_active = False
        self.power_up_cooldown = 5 * FPS  # 5 second cooldown
        self.player.deactivate_robot_form()
        print("Robot mode ended.")

    def update(self):
        # Check for 700 points to unlock robot transformation
        if self.score >= 700 and not self.power_up_unlocked:
            self.power_up_unlocked = True
            print("Level 1 Power-up Unlocked: Robot Transformation!")
            print("Press F to transform into robot for 30 seconds (once per level)")
        
        # Check for 3000 points to unlock shooting
        if self.score >= 3000 and not self.shooting_unlocked:
            self.shooting_unlocked = True
            if self.level_index == len(levels) - 1:
                self.bullets_remaining = 999  # Unlimited in final level
            else:
                self.bullets_remaining = self.max_bullets
            print("Level 2 Power-up Unlocked: Shooting!")
            print("Press WASD, QEZC, SPACE to shoot")
            if self.level_index == len(levels) - 1:
                print("UNLIMITED BULLETS in final level!")
            else:
                print(f"15 bullets per level in normal levels")
        
        # Update power-up timer
        if self.power_up_active:
            self.power_up_timer -= 1
            if self.power_up_timer <= 0:
                self.deactivate_power_up()
        
        # Update power-up cooldown
        if self.power_up_cooldown > 0:
            self.power_up_cooldown -= 1
        
        self.all_sprites.update()
        
        # Update boss attacks
        self.boss_attacks.update()

        # Check exit collision
        if self.player.rect.colliderect(self.exit_rect):
            self.sound_win.play()
            print("Level completed!")
            self.score += 100 * (self.level_index + 1)
            self.level_index += 1
            if self.level_index < len(levels):
                self.map_data = levels[self.level_index]
                self.all_sprites.empty()
                self.walls.empty()
                self.robots.empty()
                self.boss_attacks.empty()
                self.boss = None
                self.load_map()
            else:
                print("You completed all levels!")
                self.show_victory_screen()
                self.running = False

        # Check robot collision (only when robot power-up is not active)
        if not self.power_up_active:
            if pygame.sprite.spritecollideany(self.player, self.robots):
                self.sound_lose.play()
                self.lives -= 1
                pygame.time.delay(1000)

                if self.lives > 0:
                    self.all_sprites.empty()
                    self.walls.empty()
                    self.robots.empty()
                    self.boss_attacks.empty()
                    self.boss = None
                    self.load_map()
                else:
                    print("Game Over!")
                    self.sound_gameover.play()
                    self.show_game_over_screen()
                    self.running = False
        
        # Check boss attack collision
        if self.boss:
            if pygame.sprite.spritecollideany(self.player, self.boss_attacks):
                # If robot power-up is active, no damage
                if not self.power_up_active:
                    self.sound_lose.play()
                    self.lives -= 1
                    pygame.time.delay(500)
                    
                    if self.lives > 0:
                        # Reset player position
                        self.player.rect.x = self.player.start_pos[0]
                        self.player.rect.y = self.player.start_pos[1]
                        self.boss_attacks.empty()
                    else:
                        print("Game Over!")
                        self.sound_gameover.play()
                        self.show_game_over_screen()
                        self.running = False
                else:
                    # If power-up active, just destroy the attack
                    for attack in pygame.sprite.spritecollide(self.player, self.boss_attacks, True):
                        pass
            
            # Check bullet collision with boss
            for bullet in self.player.bullets:
                if self.boss.rect.colliderect(bullet.rect):
                    self.boss.take_damage(15)  # Bullets do more damage
                    bullet.kill()
                    if self.sound_boss_hit:
                        self.sound_boss_hit.play()
                    
                    # If boss is defeated
                    if self.boss.health <= 0 and not self.boss_defeated:
                        self.boss_defeated = True
                        self.score += 1000  # Big score for defeating boss
                        print("Boss defeated! +1000 points")
                        if self.sound_boss_defeat:
                            self.sound_boss_defeat.play()
                        
                        # Show boss defeat message
                        self.show_boss_defeat_message()

    def show_boss_defeat_message(self):
        """Show boss defeat message"""
        self.screen.fill((0, 0, 0))
        defeat_text = self.big_font.render("BOSS DEFEATED!", True, YELLOW)
        score_text = self.font.render(f"+1000 Points! Total: {self.score}", True, GREEN)
        bonus_text = self.font.render("Unlimited bullets activated for final battle!", True, CYAN)
        
        self.screen.blit(defeat_text, (WIDTH//2 - defeat_text.get_width()//2, HEIGHT//2 - 100))
        self.screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - 50))
        self.screen.blit(bonus_text, (WIDTH//2 - bonus_text.get_width()//2, HEIGHT//2 + 20))
        
        pygame.display.flip()
        pygame.time.delay(3000)

    def draw(self):
        self.screen.blit(self.background_img, (0, 0))

        # First draw floor
        for sprite in self.all_sprites:
            if isinstance(sprite, Floor):
                self.screen.blit(sprite.image, sprite.rect)

        # Then walls
        for sprite in self.all_sprites:
            if isinstance(sprite, Wall):
                self.screen.blit(sprite.image, sprite.rect)

        # Then exit door
        self.screen.blit(self.exit_img, self.exit_pos)

        # Then everything else
        for sprite in self.all_sprites:
            if not isinstance(sprite, (Floor, Wall)):
                self.screen.blit(sprite.image, sprite.rect)
        
        # Boss attacks
        for attack in self.boss_attacks:
            pygame.draw.circle(self.screen, RED, attack.rect.center, attack.radius)
        
        # Player bullets
        for bullet in self.player.bullets:
            pygame.draw.circle(self.screen, YELLOW, bullet.rect.center, 3)
        
        # Boss health bar
        if self.boss and self.boss.health > 0:
            self.draw_boss_health_bar()
        
        # Display info
        self.draw_hud()
        
        # Display power-up info
        self.draw_power_up_info()
        
        # Display controls guide
        self.draw_controls_guide()
        
        # Display final level bonus
        if self.level_index == len(levels) - 1:
            self.draw_final_level_bonus()
        
        pygame.display.flip()
    
    def draw_final_level_bonus(self):
        """Display final level bonus information"""
        bonus_x = WIDTH // 2
        bonus_y = HEIGHT - 100
        
        # Unlimited bullets indicator
        if not self.power_up_active:  # Only show if not in robot form
            bonus_text = self.font.render("FINAL LEVEL: UNLIMITED BULLETS!", True, YELLOW)
            self.screen.blit(bonus_text, (bonus_x - bonus_text.get_width()//2, bonus_y))
    
    def draw_power_up_info(self):
        """Display power-up information"""
        info_x = WIDTH - 250
        info_y = 80
        
        # Level 1: Robot Transformation
        if self.power_up_unlocked:
            if not self.power_up_used_this_level and self.power_up_cooldown <= 0:
                # Available to use
                power_text = self.small_font.render("F: Robot Form (30s)", True, GREEN)
                self.screen.blit(power_text, (info_x, info_y))
            elif self.power_up_active:
                # Currently active
                remaining_time = self.power_up_timer // FPS + 1
                time_text = self.small_font.render(f"Robot Form: {remaining_time}s", True, BLUE)
                self.screen.blit(time_text, (info_x, info_y))
                
                # Time bar
                bar_width = 150
                bar_height = 8
                bar_x = info_x
                bar_y = info_y + 25
                
                pygame.draw.rect(self.screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))
                time_ratio = self.power_up_timer / (self.power_up_duration * FPS)
                time_width = time_ratio * bar_width
                pygame.draw.rect(self.screen, BLUE, (bar_x, bar_y, time_width, bar_height))
            elif self.power_up_used_this_level:
                # Used this level
                used_text = self.small_font.render("Robot: Used this level", True, RED)
                self.screen.blit(used_text, (info_x, info_y))
        
        # Level 2: Shooting
        if self.shooting_unlocked:
            bullet_y = info_y + 50 if self.power_up_unlocked else info_y
            
            if self.power_up_active:
                # Can't shoot in robot form
                shoot_text = self.small_font.render("Can't shoot in Robot Form", True, ORANGE)
                self.screen.blit(shoot_text, (info_x, bullet_y))
            else:
                # Shooting available
                if self.level_index == len(levels) - 1:
                    # Final level - unlimited bullets
                    bullets_text = self.small_font.render(f"Bullets: UNLIMITED", True, YELLOW)
                    self.screen.blit(bullets_text, (info_x, bullet_y))
                    
                    # Special unlimited bar
                    bar_width = 150
                    bar_height = 8
                    bar_x = info_x
                    bar_y = bullet_y + 25
                    
                    pygame.draw.rect(self.screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))
                    # Animated unlimited bar
                    pulse = (math.sin(pygame.time.get_ticks() * 0.01) + 1) / 2  # 0 to 1
                    pulse_width = bar_width * 0.8 + bar_width * 0.2 * pulse
                    pygame.draw.rect(self.screen, CYAN, (bar_x, bar_y, pulse_width, bar_height))
                else:
                    # Normal levels - limited bullets
                    bullets_text = self.small_font.render(f"Bullets: {self.bullets_remaining}/{self.max_bullets}", True, YELLOW)
                    self.screen.blit(bullets_text, (info_x, bullet_y))
                    
                    # Bullet bar
                    bar_width = 150
                    bar_height = 8
                    bar_x = info_x
                    bar_y = bullet_y + 25
                    
                    pygame.draw.rect(self.screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))
                    bullet_ratio = self.bullets_remaining / self.max_bullets
                    bullet_width = bullet_ratio * bar_width
                    bullet_color = GREEN if bullet_ratio > 0.5 else YELLOW if bullet_ratio > 0.2 else RED
                    pygame.draw.rect(self.screen, bullet_color, (bar_x, bar_y, bullet_width, bar_height))
    
    def draw_boss_health_bar(self):
        bar_width = 250
        bar_height = 25
        bar_x = WIDTH // 2 - bar_width // 2
        bar_y = 10
        
        # Background
        pygame.draw.rect(self.screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height), 0, 5)
        pygame.draw.rect(self.screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height), 2, 5)
        
        # Health bar
        health_width = (self.boss.health / self.boss.max_health) * bar_width
        health_color = (255, 0, 0) if self.boss.health < self.boss.max_health * 0.3 else (0, 255, 0) if self.boss.health > self.boss.max_health * 0.6 else (255, 255, 0)
        pygame.draw.rect(self.screen, health_color, (bar_x, bar_y, health_width, bar_height), 0, 5)
        
        # Text
        health_text = self.font.render(f"BOSS: {self.boss.health}/{self.boss.max_health} (Lives: {self.boss.lives}/7)", True, WHITE)
        self.screen.blit(health_text, (bar_x + bar_width // 2 - health_text.get_width() // 2, bar_y + bar_height + 5))
    
    def draw_hud(self):
        # Display lives
        lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
        self.screen.blit(lives_text, (10, 10))
        
        # Display score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 50))
        
        # Display level
        level_text = self.font.render(f"Level: {self.level_index + 1}/{len(levels)}", True, WHITE)
        self.screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))
        
        # Display power level
        power_level = 0
        if self.score >= 3000:
            power_level = 2
        elif self.score >= 700:
            power_level = 1
        
        level_text = self.small_font.render(f"Power Level: {power_level}/2", True, PURPLE)
        self.screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 50))
        
        # If boss is defeated
        if self.boss_defeated:
            defeat_text = self.small_font.render("BOSS DEFEATED!", True, YELLOW)
            self.screen.blit(defeat_text, (WIDTH // 2 - defeat_text.get_width() // 2, 80))
    
    def draw_controls_guide(self):
        """Display controls guide"""
        guide_x = 10
        guide_y = HEIGHT - 150
        
        # Title
        title = self.small_font.render("Controls:", True, CYAN)
        self.screen.blit(title, (guide_x, guide_y))
        
        # Movement
        move_text = self.small_font.render("Movement: Arrow Keys (↑ ↓ ← →)", True, WHITE)
        self.screen.blit(move_text, (guide_x, guide_y + 25))
        
        # Shooting
        shoot_text = self.small_font.render("Shoot: W,A,S,D,Q,E,Z,C,SPACE", True, YELLOW)
        self.screen.blit(shoot_text, (guide_x, guide_y + 50))
        
        # Robot transformation
        if self.power_up_unlocked:
            robot_text = self.small_font.render("Robot Form: F", True, GREEN)
            self.screen.blit(robot_text, (guide_x, guide_y + 75))
    
    def show_victory_screen(self):
        self.screen.fill((0, 0, 0))
        victory_text = self.big_font.render("CONGRATULATIONS!", True, YELLOW)
        complete_text = self.font.render("You completed all levels!", True, WHITE)
        score_text = self.font.render(f"Final Score: {self.score}", True, GREEN)
        
        self.screen.blit(victory_text, (WIDTH//2 - victory_text.get_width()//2, HEIGHT//2 - 100))
        self.screen.blit(complete_text, (WIDTH//2 - complete_text.get_width()//2, HEIGHT//2))
        self.screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 + 50))
        
        pygame.display.flip()
        pygame.time.delay(5000)
    
    def show_game_over_screen(self):
        self.screen.fill((0, 0, 0))
        game_over_text = self.big_font.render("GAME OVER!", True, RED)
        score_text = self.font.render(f"Your Score: {self.score}", True, WHITE)
        restart_text = self.font.render("Press R to restart", True, YELLOW)
        
        self.screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 100))
        self.screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
        self.screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 50))
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.__init__()
                        self.run()
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        waiting = False
                        self.running = False

# Game classes
class Floor(pygame.sprite.Sprite):
    def __init__(self, pos, image, group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, image, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image, group, walls, game, robot_img):
        super().__init__(group)
        self.normal_image = image
        self.robot_image = robot_img
        self.image = self.normal_image
        self.rect = self.image.get_rect(topleft=pos)
        self.start_pos = pos
        self.walls = walls
        self.game = game
        self.normal_speed = 4
        self.robot_speed = 6
        self.speed = self.normal_speed
        self.is_robot = False
        self.bullets = pygame.sprite.Group()
        self.shoot_cooldown = 0
        self.robot_kills = 0
    
    def update(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]: dx = -self.speed
        if keys[pygame.K_RIGHT]: dx = self.speed
        if keys[pygame.K_UP]: dy = -self.speed
        if keys[pygame.K_DOWN]: dy = self.speed
        self.move(dx, dy)
        
        # In robot mode, destroy enemy robots
        if self.is_robot:
            self.destroy_enemy_robots()
        
        # Update bullets
        self.bullets.update()
        
        # Decrease shooting cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def move(self, dx, dy):
        self.rect.x += dx
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                self.rect.x -= dx
                break

        self.rect.y += dy
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                self.rect.y -= dy
                break
    
    def shoot(self, direction):
        if self.shoot_cooldown <= 0 and not self.is_robot:
            # Create bullet in specified direction
            bullet = Bullet(self.rect.centerx, self.rect.centery, self, direction)
            self.bullets.add(bullet)
            self.shoot_cooldown = 10  # Shooting delay
    
    def activate_robot_form(self):
        """Activate robot mode - now using robot_lab.png image"""
        self.is_robot = True
        self.image = self.robot_image
        self.speed = self.robot_speed
    
    def deactivate_robot_form(self):
        """Deactivate robot mode"""
        self.is_robot = False
        self.image = self.normal_image
        self.speed = self.normal_speed
    
    def destroy_enemy_robots(self):
        """In robot mode, destroy enemy robots on contact"""
        for robot in self.game.robots:
            if self.rect.colliderect(robot.rect):
                robot.kill()
                self.robot_kills += 1
                self.game.score += 10
                print(f"Enemy robot destroyed! +10 points")

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, player, direction):
        super().__init__()
        self.rect = pygame.Rect(x - 4, y - 4, 8, 8)
        self.player = player
        self.speed = 12
        
        # Determine direction based on input
        direction_map = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0),
            "up-left": (-0.707, -0.707),  # Normalized for diagonal
            "up-right": (0.707, -0.707),
            "down-left": (-0.707, 0.707),
            "down-right": (0.707, 0.707),
        }
        
        dir_x, dir_y = direction_map.get(direction, (0, -1))
        self.vx = dir_x * self.speed
        self.vy = dir_y * self.speed
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        # Remove if off-screen
        if (self.rect.bottom < 0 or self.rect.top > HEIGHT or 
            self.rect.right < 0 or self.rect.left > WIDTH):
            self.kill()
        
        # Check collision with walls
        for wall in self.player.walls:
            if self.rect.colliderect(wall.rect):
                self.kill()
                break
        
        # Check collision with enemy robots
        for robot in self.player.game.robots:
            if self.rect.colliderect(robot.rect):
                robot.kill()
                self.player.game.score += 15  # More points for shooting
                self.kill()
                print(f"Robot shot! +15 points")
                break

class Robot(pygame.sprite.Sprite):
    def __init__(self, pos, image, group, robots_group, walls):
        super().__init__(group, robots_group)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.walls = walls
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                self.speed *= -1
                self.rect.x += self.speed
                break

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos, image, group, walls, player, attacks_group, game):
        super().__init__(group)
        self.max_health = 500  # High health
        self.health = self.max_health
        self.lives = 7  # 7 lives
        self.player = player
        self.game = game
        self.attacks_group = attacks_group
        self.walls = walls
        
        if image:
            self.image = image
        else:
            # Create smaller boss for 64x64 size
            self.image = pygame.Surface((64, 64), pygame.SRCALPHA)
            
            # Main body
            pygame.draw.circle(self.image, (255, 0, 0), (32, 32), 28)
            
            # Life indicators
            for i in range(7):
                angle = (i / 7) * 2 * math.pi
                x = 32 + math.cos(angle) * 22
                y = 32 + math.sin(angle) * 22
                color = (255, 255, 0) if i < self.lives else (100, 100, 100)
                pygame.draw.circle(self.image, color, (int(x), int(y)), 6)
            
            # Eyes
            pygame.draw.circle(self.image, (0, 0, 0), (25, 25), 10)
            pygame.draw.circle(self.image, (0, 0, 0), (39, 25), 10)
            pygame.draw.circle(self.image, (255, 255, 255), (25, 25), 3)
            pygame.draw.circle(self.image, (255, 255, 255), (39, 25), 3)
        
        self.rect = self.image.get_rect(center=pos)
        self.speed = 1.5
        self.attack_cooldown = 0
        self.move_cooldown = 40
        self.direction = random.choice([-1, 1])
        self.phase = 1  # Fight phase
        self.invulnerable = False  # Temporary invulnerability
        self.invulnerable_timer = 0
    
    def update(self):
        if self.health <= 0:
            # Lose one life
            self.lives -= 1
            if self.lives > 0:
                # Recharge with less health
                self.health = self.max_health * 0.7
                self.invulnerable = True
                self.invulnerable_timer = 60  # 1 second invulnerability
                print(f"Boss lost one life! {self.lives} lives remaining")
            else:
                self.kill()
                self.game.boss_defeated = True
                return
        
        # Update invulnerability
        if self.invulnerable:
            self.invulnerable_timer -= 1
            if self.invulnerable_timer <= 0:
                self.invulnerable = False
        
        # Boss movement
        if self.move_cooldown <= 0:
            self.rect.x += self.speed * self.direction * self.phase
            self.rect.y += random.randint(-2, 2) * self.speed * self.phase
            
            for wall in self.walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.x -= self.speed * self.direction * self.phase
                    self.rect.y -= random.randint(-2, 2) * self.speed * self.phase
                    self.direction *= -1
                    break
            
            self.rect.x = max(TILESIZE, min(self.rect.x, WIDTH - self.rect.width - TILESIZE))
            self.rect.y = max(TILESIZE, min(self.rect.y, HEIGHT - self.rect.height - TILESIZE))
            
            self.move_cooldown = 40 // self.phase
        else:
            self.move_cooldown -= 1
        
        # Attack player (faster in higher phases)
        attack_speed = 60 // self.phase
        if self.attack_cooldown <= 0:
            self.attack()
            self.attack_cooldown = random.randint(attack_speed, attack_speed + 30)
        else:
            self.attack_cooldown -= 1
        
        # Change phase based on health
        if self.health < self.max_health * 0.5 and self.phase == 1:
            self.phase = 1.5
            self.speed = 2
            print("Phase 2: Boss became faster!")
        elif self.health < self.max_health * 0.3 and self.phase == 1.5:
            self.phase = 2
            self.speed = 2.5
            print("Phase 3: Boss became enraged!")
    
    def attack(self):
        # Create attack towards player
        attack = BossAttack(self.rect.center, self.player.rect.center, self)
        self.attacks_group.add(attack)
        
        # In higher phases, create more attacks
        if self.phase >= 1.5:
            for _ in range(int(self.phase)):
                offset_x = random.randint(-100, 100)
                offset_y = random.randint(-100, 100)
                target = (self.player.rect.centerx + offset_x, self.player.rect.centery + offset_y)
                attack = BossAttack(self.rect.center, target, self)
                self.attacks_group.add(attack)
    
    def take_damage(self, amount):
        if not self.invulnerable:
            self.health -= amount
            if self.health < 0:
                self.health = 0

class BossAttack(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos, boss):
        super().__init__()
        self.boss = boss
        self.radius = 10
        self.rect = pygame.Rect(start_pos[0] - self.radius, start_pos[1] - self.radius, 
                              self.radius * 2, self.radius * 2)
        self.speed = 4
        
        dx = target_pos[0] - start_pos[0]
        dy = target_pos[1] - start_pos[1]
        distance = max(1, math.sqrt(dx*dx + dy*dy))
        
        self.vx = dx / distance * self.speed
        self.vy = dy / distance * self.speed
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if (self.rect.bottom < 0 or self.rect.top > HEIGHT or 
            self.rect.right < 0 or self.rect.left > WIDTH):
            self.kill()

# Run game
if __name__ == "__main__":
    game = Game()
    game.run()