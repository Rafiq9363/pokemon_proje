import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random
import asyncio  # Eşzamansız programlama için bir kütüphane
from datetime import datetime, timedelta


class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.hp = random.randint(30, 60)
        self.power = random.randint(50, 150)
        self.last_feed_time  = datetime.now()
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]
            
            
            
class Wizard(Pokemon):  # Inherit from Pokemon
    def __init__(self, owner):
        super().__init__(owner)  # Call the parent class constructor           
            
            
            
    async def feed(self, feed_interval=60, hp_increase=10):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Pokémon'un sağlığı geri yüklenir. Mevcut sağlık: {self.hp}"
        else:
            return f"Pokémonunuzu şu zaman besleyebilirsiniz: {current_time+delta_time}"
class Wizard(Pokemon):
    async def feed(self):
        return await super().feed(hp_increase=20)
    
    
class Fighter(Pokemon):
    async def attack(self, enemy):
        super_power =random.randint(5, 15)  
        self.power += super_power
        sonuc = await super().attack(enemy)  
        self.power -= super_power
        return sonuc + f"\nDövüşçü Pokémon süper saldırı kullandı. Eklenen güç: {super_power}"
    
    
    async def feed(self):
            return await super().feed(feed_interval=15)


    async def feed(self, feed_interval=60, hp_increase=10):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Pokémon'un sağlığı geri yüklendi. Mevcut sağlık: {self.hp}"
        else:
            next_feed_time = self.last_feed_time + delta_time
            return f"Pokémonunuzu şu zaman besleyebilirsiniz: {next_feed_time.strftime('%Y-%m-%d %H:%M:%S')}"
            
    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
        async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
                    return data['forms'][0]['name']  #  Pokémon adını döndürme
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür

    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()  # Henüz yüklenmemişse bir adın geri alınması
        return f"""Pokémonunuzun ismi: {self.name}
            Pokemonun gucu: {self.power}
            Pokemonun sagligi: {self.hp}
            Pokemonun turu: {self.__class__.__name__}"""
       

    async def show_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
        async with aiohttp.ClientSession() as session:  # HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()
                    img_url = data['sprites']['front_default']# JSON yanıtının alınması ve çözümlenmesi
                    return img_url
                else:
                    return None  # İstek başarısız olursa varsayılan adı döndürür
        # PokeAPI aracılığıyla bir pokémon görüntüsünün URL'sini almak için asenktron metot
    async def attack(self, enemy):
            if isinstance(enemy, Wizard):
                chance = random.randint(1, 5)
                if chance == 1:
                    return "Sihirbaz Pokémon, savaşta bir kalkan kullandı!"
            if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ne saldırdı\n@{enemy.pokemon_trainer}'nin sağlık durumu şimdi {enemy.hp}"
            else:
                enemy.hp = 0
                return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ni yendi!"

    async def types(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    types = [t['type']['name']for t in data['types']]
                    return types
                else:
                    return None
                
                
                
if __name__ == "__main__":
    async def main():
        fighter = Fighter("username2")
        print("#" * 10)
        print(await fighter.info())
        print("#" * 10)
       
        
    asyncio.run(main())
                                        