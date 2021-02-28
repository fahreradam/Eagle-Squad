import pygame
import xml.etree.ElementTree as ET


class Tileset:
    def __init__(self, img_fname, tile_width, tile_height, columns, starting_id):
        self.img = pygame.image.load(img_fname)
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.num_columns = columns
        self.starting_id = starting_id

    def __str__(self):
        s = "[Tileset: img=" + str(self.img) + " tile_dim=(" + str(self.tile_width) + "x" + str(self.tile_height) + ")"
        s += " num_col=" + str(self.num_columns) + " start_id=" + str(self.starting_id) + "]"
        return s

class Layer:
    def __init__(self, name, id, width, height, raw_data):
        self.name = name
        self.id = id
        self.width = width
        self.height = height
        self.data = []
        lines = raw_data.split("\n")
        for i in range(len(lines)):
            num_commas = lines[i].count(",")
            if num_commas >= self.width - 1:
                new_row = []
                elements = lines[i].split(",")
                for j in range(min(len(elements), self.width)):
                    new_row.append(int(elements[j]))
                self.data.append(new_row)

    def __str__(self):
        s = "[\n"
        for i in range(self.height):
            s += "   " + str(self.data[i]) + "\n"
        return s + "]"


class Map:
    def __init__(self, path, fname):
        self.load_file(path, fname)
        self.map_width = 0
        self.map_height = 0
        self.tile_width = 0
        self.tile_height = 0
        self.tile_sets = []
        self.layers = []

    def load_file(self, path, fname):
        try:
            document = ET.parse(path + fname)
            root = document.getroot()
            self.process_file(root, path)
        except FileNotFoundError:
            print("Error opening file '" + fname + "'")

    def process_file(self, root, start_folder):
        self.map_width = int(root.attrib["width"])
        self.map_height = int(root.attrib["height"])
        self.tile_width = int(root.attrib["tilewidth"])
        self.tile_height = int(root.attrib["tileheight"])
        self.tile_sets = []
        start_index = 1
        for tset in root.iter("tileset"):
            timg = tset.find("image")
            img_fname = start_folder + timg.attrib["source"]
            twidth = int(tset.attrib["tilewidth"])
            theight = int(tset.attrib["tileheight"])
            tcolumns = int(tset.attrib["columns"])
            new_tset = Tileset(img_fname, twidth, theight, tcolumns, start_index)
            self.tile_sets.append(new_tset)
            start_index += int(tset.attrib["tilecount"])
        self.layers = []
        for layer in root.iter("layer"):
            lwidth = int(layer.attrib["width"])
            lheight = int(layer.attrib["height"])
            lid = int(layer.attrib["id"])
            lname = layer.attrib["name"]
            data = layer.find("data")
            new_layer = Layer(lname, lid, lwidth, lheight, data.text)
            self.layers.append(new_layer)

    def __str__(self):
        s = "[Map dim=(" + str(self.map_width) + "x" + str(self.map_height) + ") tile_dim=("
        s += str(self.tile_width) + "x" + str(self.tile_height) + ")\n"
        s += "\ttilesets:\n"
        for i in range(len(self.tile_sets)):
            s += "\t\t" + str(self.tile_sets[i]) + "\n"
        s += "\tlayers:\n"
        for i in range(len(self.layers)):
            s += "\t" + str(self.layers[i])

        return s

    def draw(self, surf):
        pass


M = Map("C:\\Users\\thoma\\OneDrive\\Documents\\Programming stuff\\Jason Project\\Eagle-Squad\\Library_Heist\\images\\Tiled\\", "Map 2.0.tmx")
print(M)
