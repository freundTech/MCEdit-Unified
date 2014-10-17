from PIL import Image
import zipfile
import time

def step(slot):
    texSlot = slot*16
    return texSlot
'''
Empty comment lines like:
#
are for texture spaces that I don't know what should go there
'''
textureSlots = {
    # Start Top Row
    "grass_top": (step(0),step(0)),
    "stone": (step(1),step(0)),
    "dirt": (step(2),step(0)),
    "grass_side": (step(3),step(0)),
    "planks_oak": (step(4),step(0)),
    "stone_slab_side": (step(5),step(0)),
    "stone_slab_top": (step(6),step(0)),
    "brick": (step(7),step(0)),
    "tnt_side": (step(8),step(0)),
    "tnt_top": (step(9),step(0)),
    "tnt_bottom": (step(10),step(0)),
    "web": (step(11),step(0)),
    "flower_rose": (step(12),step(0)),
    "flower_dandelion": (step(13),step(0)),
    #
    "sapling_oak": (step(15),step(0)),
    "flower_blue_orchid": (step(16),step(0)),
    "flower_allium": (step(17),step(0)),
    "flower_houstonia": (step(18),step(0)),
    "flower_tulip_red": (step(19),step(0)),
    "sapling_roofed_oak": (step(20),step(0)),
    # End Top Row

    # Start Second Row
    "cobblestone": (step(0),step(1)),
    "bedrock": (step(1),step(1)),
    "sand": (step(2),step(1)),
    "gravel": (step(3),step(1)),
    "log_oak": (step(4),step(1)),
    "log_oak_top": (step(5),step(1)),
    "iron_block": (step(6),step(1)),
    "gold_block": (step(7),step(1)),
    "diamond_block": (step(8),step(1)),
    "emerald_block": (step(9),step(1)),
    #
    "red_sand": (step(11),step(1)),
    "mushroom_red": (step(12),step(1)),
    "mushroom_brown": (step(13),step(1)),
    "sapling_jungle": (step(14),step(1)),
    "fire_layer_0": (step(15),step(1)),
    "flower_tulip_orange": (step(16),step(1)),
    "flower_tulip_white": (step(17),step(1)),
    "flower_tulip_pink": (step(18),step(1)),
    "flower_oxeye_daisy": (step(19),step(1)),
    "sapling_acacia": (step(20),step(1)),
    # End Second Row

    # Start Third Row
    "gold_ore": (step(0),step(2)),
    "iron_ore": (step(1),step(2)),
    "coal_ore": (step(2),step(2)),
    "bookshelf": (step(3),step(2)),
    "cobblestone_mossy": (step(4),step(2)),
    "obsidian": (step(5),step(2)),
    #
    "tallgrass": (step(7),step(2)),
    #
    "beacon": (step(9),step(2)),
    "dropper_front_horizontal": (step(10),step(2)),
    "crafting_table_top": (step(11),step(2)),
    "furnace_front_off": (step(12),step(2)),
    "furnace_side": (step(13),step(2)),
    "dispenser_front_horizontal": (step(14),step(2)),
    "fire_layer_1": (step(15),step(2)),
    #
    #
    #
    #
    "daylight_detector_side": (step(20),step(2)),
    # End Third Row

    # Start Fourth Row
    "sponge": (step(0), step(3)),
    "glass": (step(1), step(3)),
    "diamond_ore": (step(2), step(3)),
    "redstone_ore": (step(3), step(3)),
    #
    #
    "stonebrick": (step(6), step(3)),
    "deadbush": (step(7), step(3)),
    "fern": (step(8), step(3)),
    "dirt_podzol_top": (step(9), step(3)),
    "dirt_podzol_side": (step(10), step(3)),
    "crafting_table_side": (step(11), step(3)),
    "crafting_table_front": (step(12), step(3)),
    "furnace_front_on": (step(13), step(3)),
    "furnace_top": (step(14), step(3)),
    "sapling_spruce": (step(15), step(3)),
    #
    #
    #
    #
    # Finished Fourth Row

    # Start Fifth Row
    }

class ResourcePack:

    def __init__(self, zipfile, name):
        self.zipfile = zipfile
        self.pack_name = name
        self.block_image = {}
        self.old_terrain = Image.open('terrain.png')

        self.open_pack()

    def open_pack(self):
        zfile = zipfile.ZipFile(self.zipfile)
        for name in zfile.infolist():
            if name.filename.endswith(".png"):
                #print name.filename
                if name.filename.startswith("assets/minecraft/textures/blocks"):
                    #print "Block Texture!"
                    print name.filename.split("/")[-1]
                    block_name = name.filename.split("/")[-1]
                    block_name = block_name.split(".")[0]
                    zfile.extract(name.filename, "textures/")
                    possible_texture = Image.open("textures/"+name.filename)
                    if possible_texture.size == (16, 16):
                        self.block_image[block_name] = Image.open("textures/"+name.filename)
                    else:
                        self.block_image[block_name] = Image.open("textures/"+name.filename).crop((0,0,16,16))
        self.parse_terrain_png()

    # FIXME: Use a Dictionary to find out were to put the textures
    def parse_terrain_png(self):
        new_terrain = Image.new("RGBA", (512, 512), None)
        for tex in self.block_image.keys():
            try:
                image = self.block_image[tex]
                slot = textureSlots[tex]
                new_terrain.paste(image, slot, image)
            except:
                pass       
        # Do special blocks
        # Start Ender Chest
        ender_copy = self.old_terrain.copy()
        ender_front = ender_copy.crop((step(16),step(2),step(16)+16,step(2)+16))
        new_terrain.paste(ender_front, (step(16), step(2)), ender_front)

        ender_top = ender_copy.crop((step(17),step(2),step(17)+16,step(2)+16))
        new_terrain.paste(ender_top, (step(17), step(2)), ender_top)

        ender_side = ender_copy.crop((step(18),step(2),step(18)+16,step(2)+16))
        new_terrain.paste(ender_side, (step(18), step(2)), ender_side)
        
        
        new_terrain.save(self.pack_name.replace(" ", "_")+".png")
        new_terrain.show()
rp = ResourcePack('OCD pack 1.8.zip', "OCD Pack")
