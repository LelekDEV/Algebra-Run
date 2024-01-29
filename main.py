import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()

clicked = False

def load_level(name):
	data = []

	with open(f'{name}.lvl', 'r') as file:
		for line in file:
			obj = []
			temp = ''
			i = 0
			while i < len(line):
				if line[i] == '-':
					i += 1
					continue
				elif line[i] == ' ':
					obj.append(int(temp))
					temp = ''
				else:
					temp += line[i]
				i += 1
			data.append(obj)

	grouped_data = []

	for obj in data:
		if not obj:
			grouped_data.append([])
			continue

		grouped_obj = []

		for i in range(0, len(obj), 2):
			grouped_obj.append((obj[i], obj[i + 1]))

		grouped_data.append(grouped_obj)

	return grouped_data

def save_level(*data):
	with open('level.lvl', 'w') as file:
		for i, obj in enumerate(data):
			if not obj:
				file.write('-')
			else:
				line = ''
				for pos in obj:
					for x in pos:
						line += f'{x} '
				file.write(line)
			if i != len(data) - 1:
				file.write('\n')

def get_block_rects():
	rects = []
	for pos in blocks:
		rects.append(pygame.Rect(((pos[0] * 128, screen.get_height() - (pos[1] + 1) * 128), (128, 128))))
	return rects

def get_spike_rects():
	rects = []
	for pos in spikes:
		rects.append(pygame.Rect(((pos[0] * 128 + 52, screen.get_height() - (pos[1] + 1) * 128 + 40), (24, 48))))
	return rects

def get_orb_rects():
	rects = []
	for pos in orbs:
		rects.append(pygame.Rect(((pos[0] * 128, screen.get_height() - (pos[1] + 1) * 128), (128, 128))))
	return rects

class Group(pygame.sprite.Group):
	def __init__(self):
		super().__init__()

		self.pos = pygame.math.Vector2()

		self.image_block = pygame.image.load('block.png').convert()
		self.image_block = pygame.transform.scale(self.image_block, (128, 128))

		self.image_spike = pygame.image.load('spike.png').convert_alpha()
		self.image_spike = pygame.transform.scale(self.image_spike, (128, 128))

		self.image_orb = pygame.image.load('orb.png').convert_alpha()
		self.image_orb = pygame.transform.scale(self.image_orb, (128, 128))

	def draw(self):
		for pos in blocks:
			screen.blit(self.image_block, (pos[0] * 128 - self.pos.x, screen.get_height() - (pos[1] + 1) * 128 - self.pos.y))

		for pos in spikes:
			image = self.image_spike.copy()

			if pos in rotated_tiles:
				image = pygame.transform.flip(image, False, True)

			screen.blit(image, (pos[0] * 128 - self.pos.x, screen.get_height() - (pos[1] + 1) * 128 - self.pos.y))

		for pos in orbs:
			screen.blit(self.image_orb, (pos[0] * 128 - self.pos.x, screen.get_height() - (pos[1] + 1) * 128 - self.pos.y))

		if mode == 'play':
			new_image = pygame.transform.rotate(player.image, player.rotation)

			dx = new_image.get_width() - player.image.get_width()
			dy = new_image.get_height() - player.image.get_height()

			screen.blit(new_image, (player.rect.x - dx / 2 - self.pos.x, player.rect.y - dy / 2 - self.pos.y))

		if show_hitboxes:
			for rect in get_block_rects():
				pygame.draw.rect(screen, [0, 0, 255], (rect.topleft - self.pos, rect.size), 4)

			for rect in get_spike_rects():
				new_rect = rect.copy()
				new_rect.center -= self.pos
				pygame.draw.rect(screen, [255, 0, 0], (rect.topleft - self.pos, rect.size), 4)

			pygame.draw.rect(screen, [255, 0, 0], (player.rect.topleft - self.pos, player.rect.size), 4)

			if len(player.trail) >= 2:
				pygame.draw.lines(screen, [0, 255, 0], False, [tuple(pos - self.pos) for pos in player.trail], 4)

	def follow_player(self):
		self.pos.x += player.pos.x - self.pos.x - 400

class Player(pygame.sprite.Sprite):
	def __init__(self, group):
		super().__init__(group)

		self.image = pygame.image.load('cube.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (128, 128))

		self.pos = pygame.math.Vector2(0, screen.get_height() - 64)
		self.rect = self.image.get_rect(center = self.pos)
		self.vel = pygame.math.Vector2()

		self.rotation = 5

		self.grounded = False

		self.vel.x = 16

		self.trail = []

	def update(self):
		for rect in get_spike_rects():
			if self.rect.colliderect(rect):
				pass#self.kill()

		self.trail.append(self.pos.copy())

		self.pos.x += self.vel.x
		self.rect.centerx = self.pos.x

		self.vel.y += 2.2

		self.pos.y += self.vel.y
		self.rect.centery = self.pos.y

		self.rect.y += 1

		for rect in get_orb_rects():
			if self.rect.colliderect(rect):
				if pygame.key.get_pressed()[pygame.K_UP]:
					self.vel.y = -32

		for rect in get_block_rects():
			if self.rect.colliderect(rect):
				self.vel.y = 0
				self.rect.bottom = rect.top
				self.pos.y = self.rect.centery

				if not self.grounded:
					self.rotation = (self.rotation + 45) // 90 * 90

				if pygame.key.get_pressed()[pygame.K_UP]:
					self.vel.y = -36

				self.grounded = True

				return

		if self.pos.y > screen.get_height() - 64:
			self.vel.y = 0
			self.rect.bottom = screen.get_height()
			self.pos.y = self.rect.centery

			if not self.grounded:
				self.rotation = (self.rotation + 45) // 90 * 90

			if pygame.key.get_pressed()[pygame.K_UP]:
				self.vel.y = -36

			self.grounded = True

		else:
			self.rotation -= 6

			self.grounded = False

	def kill(self):
		global mode
		mode = 'edit'
		pygame.mixer.music.stop()

group = Group()
player = Player(group)

blocks, spikes, orbs, rotated_tiles = load_level('level')

mode = 'play'
switch_mode_cooldown = False
edit_mode = blocks

show_hitboxes = False
switch_show_hitboxes_cooldown = False

pygame.mixer.music.load('song.ogg')
pygame.mixer.music.play()

while True:
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

	if pygame.key.get_pressed()[pygame.K_TAB]:
		if not switch_mode_cooldown:
			if mode == 'play':
				mode = 'edit'
				pygame.mixer.music.stop()
			else:
				mode = 'play'

				player.pos.x = 0
				player.pos.y = screen.get_height() - 64
				player.rect.center = player.pos

				player.vel.x = 16
				player.vel.y = 0

				player.rotation = 0

				player.trail = []

				pygame.mixer.music.play()

			switch_mode_cooldown = True
	else:
		switch_mode_cooldown = False

	if pygame.key.get_pressed()[pygame.K_w]:
		if not switch_show_hitboxes_cooldown:
			show_hitboxes = not show_hitboxes

		switch_show_hitboxes_cooldown = True
	else:
		switch_show_hitboxes_cooldown = False

	if mode == 'play':
		player.update()
		group.follow_player()

	if mode == 'edit':
		keys = pygame.key.get_pressed()

		if keys[pygame.K_1]:
			edit_mode = blocks
		if keys[pygame.K_2]:
			edit_mode = spikes
		if keys[pygame.K_3]:
			edit_mode = orbs
		if keys[pygame.K_4]:
			edit_mode = rotated_tiles

		pos = (int((pygame.mouse.get_pos()[0] + group.pos.x) // 128), int((screen.get_height() - pygame.mouse.get_pos()[1]) // 128))

		if pygame.mouse.get_pressed()[0]:
			if not pos in edit_mode:
				edit_mode.append(pos)
		elif pygame.mouse.get_pressed()[2]:
			if pos in blocks: blocks.remove(pos)
			if pos in spikes: spikes.remove(pos)
			if pos in orbs: orbs.remove(pos)
			if pos in rotated_tiles: rotated_tiles.remove(pos)

		if pygame.key.get_pressed()[pygame.K_q]:
			save_level(blocks, spikes, orbs, rotated_tiles)

		if pygame.key.get_pressed()[pygame.K_LEFT]:
			group.pos.x -= 10

		if pygame.key.get_pressed()[pygame.K_RIGHT]:
			group.pos.x += 10

	screen.fill([255, 255, 255])

	if mode == 'edit':
		for x in range(16):
			pygame.draw.line(screen, [0, 0, 0], (x * 128 - group.pos.x % 128, 0), (x * 128 - group.pos.x % 128, screen.get_height()))
		for y in range(9):
			pygame.draw.line(screen, [0, 0, 0], (0, y * 128 + screen.get_height() % 128), (screen.get_width(), y * 128 + screen.get_height() % 128))

	group.draw()

	pygame.display.update()