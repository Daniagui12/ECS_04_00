
from src.engine.service_locator import ServiceLocator


class CPlayerWeapon:
    def __init__(self, weapon: str, player_info: dict):
        self.weapon = weapon
        self.cooldown = player_info["triple_shot_cooldown"]
        self.player_info = player_info
        self.sprite = self.player_info["image"]
    
    def set_weapon(self):
        if self.sprite is None:
            self.sprite = self.player_info["image"]
            self.weapon = "basic"
        
        elif self.sprite == self.player_info["alternate_image"] and self.cooldown <= 0.0:
            self.sprite = self.player_info["image"]
            self.weapon = "basic"
        
        elif self.sprite == self.player_info["image"] and self.cooldown <= 0.0:
            self.sprite = self.player_info["alternate_image"]
            self.weapon = "multiple"