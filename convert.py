import subprocess


def convert(file, convertedFormat):
        try:
            bashCommand = "ebook-convert {0} {1}".format(file, convertedFormat)
            output = subprocess.check_output(["bash", "-c", bashCommand])
            print("Succesful conversion! {} file created.".format(convertedFormat))
            return output

        except Exception:
            print("""\n Oops. You file could not be converted. \n Check the calibre documentation here: https://manual.calibre-ebook.com/conversion.html#conversion""")
