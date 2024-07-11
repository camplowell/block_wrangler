# Developer README

## Importing blocks and tags

The import.sh script can be used to import blocks and tags from the Minecraft [data generator](https://wiki.vg/Data_Generators).
Specifically, it can import blocks from the `--reports` command, and block tags from the `--server` command.

### Running on a Vanilla server

On versions since Minecraft 1.18, the data generator can be called using the following command:
```bash
java -DbundlerMainClass=net.minecraft.data.Main -jar minecraft_server.jar
```

Pre-1.18, the server used to be a monolithic jar, and the data generator was called using the following command:
```bash
java -cp minecraft_server.jar net.minecraft.data.Main
```

### Running in a modded environment

In a modded environment, the documentation behind how to run the data generator becomes more sparse.
Here's what I was able to find:
[Data generation on Fabric](https://fabricmc.net/wiki/tutorial:datagen_setup)
[Data generation on Forge](https://docs.minecraftforge.net/en/latest/datagen/)