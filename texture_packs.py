from PIL import Image
import zipfile
import time

def step(slot):
    texSlot = slot*16
    return texSlot

unknown_textures = [
    (step(14),step(0)),
    (step(9),step(1)),
    (step(6),step(2)),
    (step(8),step(2)),
    (step(4),step(3)),
    (step(5),step(3)),
    ]
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
    # End Fourth Row

    # Start Fifth Row
    "wool_colored_white": (step(0), step(4)),
    "mob_spawner": (step(1), step(4)),
    "snow": (step(2), step(4)),
    "ice": (step(3), step(4)),
    "grass_side_snowed": (step(4), step(4)),
    "cactus_top": (step(5), step(4)),
    "cactus_side": (step(6), step(4)),
    "cactus_bottom": (step(7), step(4)),
    "clay": (step(8), step(4)),
    "reeds": (step(9), step(4)),
    "jukebox_side": (step(10), step(4)),
    "jukebox_top": (step(11), step(4)),
    "waterlily": (step(12), step(4)),
    "mycelium_side": (step(13), step(4)),
    "mycelium_top": (step(14), step(4)),
    "sapling_birch": (step(15), step(4)),
    #
    #
    "dropper_front_vertical": (step(18), step(4)),
    "daylight_detector_inverted_top": (step(19), step(4)),
    # End Fifth Row

    # Start Sixth Row
    "torch_on": (step(0), step(5)),
    "door_wood_upper": (step(1), step(5)),
    "door_iron_upper": (step(2), step(5)),
    "ladder": (step(3), step(5)),
    "trapdoor": (step(4), step(5)),
    "iron_bars": (step(5), step(5)),
    "farmland_wet": (step(6), step(5)),
    "farmland_dry": (step(7), step(5)),
    "wheat_stage_0": (step(8), step(5)),
    "wheat_stage_1": (step(9), step(5)),
    "wheat_stage_2": (step(10), step(5)),
    "wheat_stage_3": (step(11), step(5)),
    "wheat_stage_4": (step(12), step(5)),
    "wheat_stage_5": (step(13), step(5)),
    "wheat_stage_6": (step(14), step(5)),
    "wheat_stage_7": (step(15), step(5)),
    #
    #
    "dispenser_front_vertical": (step(18), step(5)),
    #
    # End Sixth Row

    # Start Seventh Row
    "lever": (step(0), step(6)),
    "door_wood_lower": (step(1), step(6)),
    "door_iron_lower": (step(2), step(6)),
    "redstone_torch_on": (step(3), step(6)),
    "stonebrick_mossy": (step(4), step(6)),
    "stonebrick_cracked": (step(5), step(6)),
    "pumpkin_top": (step(6), step(6)),
    "netherrack": (step(7), step(6)),
    "soul_sand": (step(8), step(6)),
    "glowstone": (step(9), step(6)),
    "piston_top_sticky": (step(10), step(6)),
    "piston_top_normal": (step(11), step(6)),
    "piston_side": (step(12), step(6)),
    "piston_bottom": (step(13), step(6)),
    "piston_inner": (step(14), step(6)),
    "pumpkin_stem_disconnected": (step(15), step(6)),
    #
    #
    #
    # End Seventh Row

    # Start Eigth Row
    "rail_normal_turned": (step(0),step(7)),
    "wool_colored_black": (step(1),step(7)),
    "wool_colored_gray": (step(2),step(7)),
    "redstone_torch_off": (step(3),step(7)),
    "log_spruce": (step(4),step(7)),
    "log_birch": (step(5),step(7)),
    "pumpkin_side": (step(6),step(7)),
    "pumpkin_face_off": (step(7),step(7)),
    "pumpkin_face_on": (step(8),step(7)),
    "cake_top": (step(9),step(7)),
    "cake_side": (step(10),step(7)),
    "cake_inner": (step(11),step(7)),
    "cake_bottom": (step(12),step(7)),
    "mushroom_block_skin_red": (step(13),step(7)),
    "mushroom_block_skin_brown": (step(14),step(7)),
    "pumpkin_stem_connected": (step(15),step(7)),
    #
    #
    #
    #
    # End Eigth Row
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
                        if possible_texture.size == (32, 32):
                            self.block_image[block_name] = Image.open("textures/"+name.filename).resize((16, 16))
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
        copy = self.old_terrain.copy()
        ender_front = copy.crop((step(16),step(2),step(16)+16,step(2)+16))
        new_terrain.paste(ender_front, (step(16), step(2)), ender_front)

        ender_top = copy.crop((step(17),step(2),step(17)+16,step(2)+16))
        new_terrain.paste(ender_top, (step(17), step(2)), ender_top)

        ender_side = copy.crop((step(18),step(2),step(18)+16,step(2)+16))
        new_terrain.paste(ender_side, (step(18), step(2)), ender_side)

        ender_bottom = copy.crop((step(19),step(2),step(19)+16,step(2)+16))
        new_terrain.paste(ender_bottom, (step(19), step(2)), ender_bottom)
        # End Ender Chest

        # Start Normal Chest
        normal_top = copy.crop((step(16),step(3),step(16)+16,step(3)+16))
        new_terrain.paste(normal_top, (step(16), step(3)), normal_top)

        normal_side = copy.crop((step(17),step(3),step(17)+16,step(3)+16))
        new_terrain.paste(normal_side, (step(17),step(3)), normal_side)

        normal_front = copy.crop((step(18),step(3),step(18)+16,step(3)+16))
        new_terrain.paste(normal_front, (step(18),step(3)), normal_front)

        idk = copy.crop((step(19),step(3),step(19)+16,step(3)+16))
        new_terrain.paste(idk, (step(19),step(3)), idk)
        # End Normal Chest

        # Start Double Chest
        double_front = copy.crop((step(16),step(4),step(16)+step(2),step(4)+16))
        new_terrain.paste(double_front, (step(16), step(4)), double_front)

        double_back = copy.crop((step(16),step(5),step(16)+step(2),step(5)+16))
        new_terrain.paste(double_back, (step(16), step(5)), double_back)
        # End Double Chest

        # Start Trapped Chest
        trapped_top = copy.crop((step(16),step(6),step(16)+16,step(6)+16))
        new_terrain.paste(trapped_top, (step(16),step(6)), trapped_top)

        trapped_side = copy.crop((step(17),step(6),step(17)+16,step(6)+16))
        new_terrain.paste(trapped_side, (step(17),step(6)), trapped_side)

        trapped_front = copy.crop((step(18),step(6),step(18)+16,step(6)+16))
        new_terrain.paste(trapped_front, (step(18),step(6)), trapped_front)
        # End Trapped Chest

        # Start Double Trapped Chest
        trapped_double_front = copy.crop((step(16),step(7),step(16)+step(2),step(7)+step(2)))
        new_terrain.paste(trapped_double_front, (step(16),step(7)), trapped_double_front)
        

        unknown_tex = copy.crop((step(31),step(31),step(31)+16,step(31)+16))
        for coord in unknown_textures:
            new_terrain.paste(unknown_tex, coord, unknown_tex)
        
        
        new_terrain.save(self.pack_name.replace(" ", "_")+".png")
        new_terrain.show()
rp = ResourcePack('OCD pack 1.8.zip', "OCD Pack")
