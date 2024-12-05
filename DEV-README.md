# Developer README

## Setting up a development environment
first, set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

then, install an editable versiion of `block_wrangler` with the development dependencies:
```bash
pip install -e .[dev]
```

You're ready to go!

## Importing blocks and tags

The import.sh script can be used to import blocks and tags from the Minecraft [data generator](https://wiki.vg/Data_Generators) (If the link is down, here is a link to it on the [Wayback Machine](https://web.archive.org/web/https://wiki.vg/Data_Generators)).


### Running on a Vanilla server

On versions since Minecraft 1.18, the data generator can be called using the following command:
```bash
java -DbundlerMainClass=net.minecraft.data.Main -jar minecraft_server.jar [--reports] [--server]
```

Pre-1.18, the server used to be a monolithic jar, and the data generator was called using the following command:
```bash
java -cp minecraft_server.jar net.minecraft.data.Main [--reports] [--server]
```

The relevant arguments for this script are:
`--reports` produces the list of blocks and their states.
`--server` produces a list of block tags.


### Running in a modded environment

In a modded environment, the documentation behind how to run the data generator becomes more sparse.
Here's what I was able to find:
[Data generation on Fabric](https://fabricmc.net/wiki/tutorial:datagen_setup)
[Data generation on Forge](https://docs.minecraftforge.net/en/latest/datagen/)

You will likely need to run this in a development environment, rather than on the final server jar.

### Running the import script
Once you've generated the data, you should see a `generated` folder next to `server.jar`.

Ensure you are using the development virtual environment, then run the import script:
```bash
python ./scripts/importer.py data-generator /path/to/mc_server/generated
```
This will import all blocks and tags from the data generator.