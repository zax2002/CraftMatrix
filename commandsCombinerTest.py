from modules.minecraft.rconManager import RconManager
from modules.minecraft.minecraftUtils import MinecraftUtils
from modules.config import Config


config = Config("./config.json")

rconManager = RconManager(config)
rconManager.connect()

minecraftUtils = MinecraftUtils(config, rconManager)

# minecraftUtils.runMultipleCommands((
# 	"say 1",
# 	"say 2",
# 	"say 3",
# 	"say 4"
# ))

combined = []
for y in range(64):
	for x in range(96):
		combined.append(f"setblock {-48 + x} {68 + y} -30 redstone_block")

minecraftUtils.runMultipleCommands(combined)