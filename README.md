# AWBWReplayRecorder

[![AWBW Logo](./media/awbwlogo.gif)](https://awbw.amarriner.com/)

These scripts were created to save replays from the awesome website [Advance Wars by Web](https://awbw.amarriner.com/) to gif or movie files. The code works by taking snapshots of the replays at each turn (through [Selenium](https://selenium-python.readthedocs.io/)) and compiling the snapshots into gif files through [ImageMagick](https://imagemagick.org/index.php).


![AWBW Logo](./media/M_turn_038.jpg)

## Instructions

First time setup and use are still a bit clunky but I'm making improvements in usability as time allows.

### Installation and Setup

1. Download the [Selenium driver for Chrome](https://chromedriver.chromium.org/downloads).
2. Place the file in a folder (ideally `./chromedriver/chromedriver` relative to the scripts folder).
3. Install ImageMagick for `gif` export.
4. Install the [conda environment](https://github.com/Chipdelmal/AWBWReplayRecorder/tree/main/conda) or the required python packages independently (see **Dependencies**).

### Use


## Dependencies

* [Selenium](https://selenium-python.readthedocs.io/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [ImageMagick](https://imagemagick.org/index.php)


# Author

<img src="./media/pusheen.jpg" height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/blog/)
