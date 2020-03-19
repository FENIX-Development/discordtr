import discord

def bul(guild, ID: int):
  if ID is None:
    raise TypeError('bir ID verisi girilmeli')
  else:
    if discord.utils.get(guild.channels, id=ID):
      if not ID:
        raise KeyError('geçersiz ID')
      else:
        return discord.utils.get(guild.channels, id=ID)
    elif discord.utils.get(guild.members, id=ID):
      if not ID:
        raise KeyError('geçersiz ID')
      else:
        return discord.utils.get(guild.members, id=ID)
    elif discord.utils.get(guild.roles, id=ID):
      if not ID:
        raise KeyError('geçersiz ID')
      else:
        return discord.utils.get(guild.roles, id=ID)

#def kanal(self, guild, kanalID):
#  if kanalID is None:
#    raise TypeError('hata')
#  return '' if not kanalID else discord.utils.get(guild.channels, id=int(kanalID))
#
#def kullanici(self, guild, kullaniciID):
#  if kullaniciID is None:
#    raise TypeError('hata')
#  return '' if not kullaniciID else discord.utils.get(guild.members, id=int(kullaniciID))


class Emoji:

  def __init__(self, client):
    self.client = client

  def emoji_id(self, guild, emojiAdi):
    x = discord.utils.get(guild.emojis, name=str(emojiAdi))
    return 'Hata: Geçerli bir emoji adı girmelisin!' if not x else f'**{emojiAdi}** isimli emojinin **ID**: `{x.id}`'

  def emoji(self, guild, emojiID):
    x = discord.utils.get(guild.emojis, id=int(emojiID))
    return 'Hata: Geçerli bir emoji ID girmelisin' if not x else f'**{x}**'

  def emojiler(self, guild):
    x = guild.emojis
    if not x:
      raise KeyError('Hata: Emoji belirlenemedi')
    else:
      return f'{"".join([str(y) for y in x])}'

class Bilgi:

  def __init__(self, client):
    self.client = client

  def ping(self):
    return 'Hata: Belirsiz' if not self.bot else f'{round(self.bot.latency * 1000)} milisaniye'

class Bot:

  def __init__(self, client):
    self.client = client

  def tum_sunucular(self):
    return 'Hata: Belirsiz' if not self.guilds else self.guilds

  def tum_kullanicilar(self):
    return 'Hata: Belirsiz' if not self.users else self.users

  async def sil(self, channel, miktar):
      return '' if not miktar else await channel.purge(limit=int(miktar))

  async def ban(self, message, kullaniciID: int):
    banlayan = message.author
    sunucu = banlayan.guild
    banlanan = sunucu.get_member(kullaniciID)
    if kullaniciID == int(message.author.id):
        raise KeyError(f'{kullaniciID} ban fonksiyonu için geçerli bir anahtar değil.')
    else:
      if banlanan is not None:
          return await sunucu.ban(banlanan)
      else:
        if not kullaniciID:
          raise KeyError('Hata: Kullanıcı ID girilmedi')
        else:
          return await self.http.ban(kullaniciID, sunucu.id, 0)

  async def kick(self, message, kullaniciID: int):
    atan = message.author
    sunucu = atan.guild
    atilan = sunucu.get_member(kullaniciID)
    if kullaniciID == int(message.author.id):
      raise KeyError(f'{kullaniciID} kick fonksiyonu için geçerli bir anahtar değil.')
    else:
      if atilan is not None:
        return await sunucu.kick(atilan)
      else:
        raise KeyError(f'{kullaniciID} kick fonksiyonu için geçerli bir anahtar değil.')

  def bul(self, ID: int):
    if ID is None:
      raise TypeError('bir ID verisi girilmeli')
    else:
      if discord.utils.get(self.guilds, id=ID):
        if not ID:
          raise KeyError('geçersiz ID')
        else:
          return discord.utils.get(self.guilds, id=ID)
      elif discord.utils.get(self.users, id=ID):
        if not ID:
          raise KeyError('geçersiz ID')
        else:
          return discord.utils.get(self.users, id=ID)