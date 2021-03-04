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
        self.root = None
        self.load_file(path, fname)


    def load_file(self, path, fname):
        try:
            document = ET.parse(path + fname)
            self.root = document.getroot()
            self.process_file(self.root, path)
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
        self.data = []
        for layer in root.iter("layer"):
            lwidth = int(layer.attrib["width"])
            lheight = int(layer.attrib["height"])
            lid = int(layer.attrib["id"])
            lname = layer.attrib["name"]
            data = layer.find("data")
            new_layer = Layer(lname, lid, lwidth, lheight, data.text)
            self.layers.append(new_layer)
            for x in range(0, new_layer.width):
                row = new_layer.data[x]
                # print(row)
                for y in range(0, len(row)):
                    # print(row[y])
                    self.data.append(row[y])
            # print(new_layer)
        # for j in range(0, len(self.layers)):
        #     for y in range(0, self.layers[0].height):
        #         for x in range(0, self.layers[0].width):
        #             self.data.append(self.layers[j].data[x][y])
                    # print(self.layers[j].data[x])

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

    def draw(self, surf, root):
        self.win = surf
        self.tile_width = int(root.attrib["tilewidth"])
        self.tile_height = int(root.attrib["tileheight"])
        self.tile_spacing = 1
        self.tile_count = 486
        self.tile_columns = 27
        self.tile_rows = (self.tile_count / self.tile_columns)
        self.img = pygame.image.load("C:\\Users\\thoma\\OneDrive\\Documents\\Programming stuff\\Jason Project\\Eagle-Squad\\Library_Heist\\images\\Tiled\\roguelikeIndoor_transparent.png")
        # print(self.layers[0].data)
        x = 1
        y = 1
        for j in range(0, len(self.layers)):
            chunk_min = 2500 * j
            x = 1
            y = 1
            for tile_num in range(0, (self.layers[j].width * self.layers[j].height)):

                ssheet_row = 0
                ssheet_column = 0
                rangeMax = 0
                for i in range(1, int(self.tile_rows)):
                    # print(tile_num)
                    if self.data[tile_num + chunk_min] < i * self.tile_columns:
                        ssheet_row = i
                        rangeMax = i * self.tile_columns
                        break

                fromLeft = rangeMax - self.data[tile_num + chunk_min]+1
                ssheet_column += self.tile_columns - fromLeft
                self.win.blit(self.img, (y * self.tile_width, x * self.tile_height), (ssheet_column * (self.tile_width + self.tile_spacing),
                              ssheet_row * (self.tile_height + self.tile_spacing), self.tile_width, self.tile_height))
                x += 1
                if x == self.layers[j].width:
                    x = 1
                    y += 1
