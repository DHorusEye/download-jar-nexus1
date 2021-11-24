import wget


def downjar(components_list):
    for item in components_list:

        path = item["assets"][0]["path"]
        newPath = path.split("/")
        fileurl = item["assets"][0]["downloadUrl"]
        filePath = r"C:\Users\yakirv\Desktop\Nexus-Downloads"
        endPath = filePath + "\\" + newPath[-1]
        wget.download(fileurl, endPath)


