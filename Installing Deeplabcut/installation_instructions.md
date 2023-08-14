Downloading DLC on your computer:
1. Install Anaconda
2. Install Git
    Windows specific git
3. In your computer's command prompt (Windows + r, type cmd and then enter on Windows, idk how to do it on Mac), navigate to where you want to place DeepLabCut
4. Type git clone https://github.com/DeepLabCut/DeepLabCut.git
5. Once that has finished, type cd DeepLabcut\conda-environments
6. If you type dir on Windows, you should see a file called DEEPLABCUT.yaml
7. Type conda env create -f DEEPLABCUT.yaml
    This should create a new environment called DEEPLABCUT that will contain all the dependencies for the package
8. Whenever you want to use this environment, follow the instructions from the other pinned message. Good   luck!

Running on the computer:
1. Open Anaconda Navigator
2. Launch cmd.exe
3. Type conda activate DEEPLABCUT
    Note that this environment's name is in all caps. That's what the config.yaml file from DLC automatically names it as, so be sure to write in all caps when calling it
    Once in the conda environment, you should see (DEEPLABCUT) written on the lefthand side, where it said (base) before
    The environment should have all dependencies installed, and once you have activated it, you have access to them. If you need to launch another terminal/command prompt to run something DLC related, repeat steps 1-3; a new cmd.exe prompt will not natively enter this environment. To deactivate, type conda deactivate. This will bring you back to the base environment.
4. Now, to run the DLC user interface, type python -m deeplabcut
    Note that this is all lower case now; here we are calling the deeplabcut package, not the environment, so we must use all lowercase
5. You will see the options to create a new project, or load a project. Select whichever you'd like to use
    Create new project will be for a new network/application of DLC on a new paradigm
    Load a project will be to pick up wherever you left off on a different project you already created. Say you labeled some data but want to add more videos/frames to the training set, or didn't finish labeling data last time, you'll select this option

Creating a new project
1. You will be prompted to add an author (your name) and a project (likely "stroke" or some other subsidiary; like if you are looking at paws in one network you may say "stroke_paw").
    I recommend using underscores or hyphens instead of spaces --- spaces in file names have a tendency to mess up operating system operations, especially on windows. Will just prevent potentially weird, hard to identify bugs down the line
2. Select the location you'd like the project to be made in (which folder) and the videos you'd like to include from the browse button.
    You will select a folder containing videos, and it will automatically select all videos in that folder. You can then manually deselect any you don't want included from the User Interface
    I also prefer to select to copy the videos to the project folder, but this is not necessary.
3. Once you create the project, a file structure will be created that includes a new config.yaml file, among other folders/files. If you later want to load this project to pick up where you left off, you will navigate to the folder of the format author-projectname-date. The config.yaml file will be in this file structure, and you will select this file when loading.
    You can go into this config file and edit the body parts being tracked for your own purposes. I believe there are 4 parts automatically labeled, bodypart1 , bodypart2 , bodypart3, and objectA; or something like that. You can add and remove bodyparts, as well as rename them (i.e. leftpaw, rightpaw, snout, etc) for ease of labelling.
4. Next, you will proceed to extracting frames. I think it's fine to use the default values for everything here (i.e. the algorithm used, and let them automatically determine which frames to pick). You can keep extracting more frames, if you've determined you want more than they initially selected for you.
    The amount the algorithm extracts depends on how many videos & the length of each. The amount you'll need depends on the variability in your training vs test data sets, and what variability they've captured (lighting conditions, camera angles, etc). I recommend at least briefly going through the extracted frames before labelling to make sure you're satisfied. If you label frames and then decide you want more frames, there's no problem -- you can reload the project and extract more, and just label the additional ones. Your previous labelling should be saved.
5. Now, you'll proceed to labelling the body parts. I think this is called something like Label Frames on the GUI. You will label the body parts in order on each frame. On the left hand panel, near the top, you'll see 4 options. Select the one that looks like a plus sign to add labels to the frame. These will be dots colored to coordinate with the body part they are representing. If you misclick and want to move a dot, select from those 4 options on the upper left the one that looks like a computer mouse arrow, and then select and drag the dot you want to move. You can use the left and right arrows on your keyboard to move between frames to label.
6. When you want to stop labelling (whether you've gone through all the extracted frames, or just want to take a break and close the UI, select the layer in the lefthand panel that contain your dots (I think it'll be the top layer of the two displayed). Then, go to File-> Save selected layer, and the labels should be saved.
    You can verify this saved properly by going into your project folder, then the labeled-data subfolder, then the subfolder for whichever video you just labelled, and check that alongside the extracted frames there are 2 new files: an excel/csv file, and a .h5 file. These will contain the label locations for the training step of the network.