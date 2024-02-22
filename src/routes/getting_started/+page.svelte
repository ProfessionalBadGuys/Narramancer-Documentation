<div class="section">
<h2 id="installation">Installation</h2>
<p>Import the Narramancer Unity package into your project</p>
</div>

<div class="section">
<h2 id="settings">Set Api Settings</h2>
<p>Because Narramancer depends on Odin Serializer, the .NET Api for your project must be set to 4.x.</p>
<p>Go to Project Settings -> Player -> Other Settings and Change Api Compatibility Level to “.NET 4.x”</p>
</div>

<div class="section">
<h2 id="initialization">Initialization</h2>
<p>Before using Narrmanacer for the first time, you must trigger initialization by opening the Narramancer window.</p>
<p>Open the Narramancer Window by choosing  ‘Window -> Narramancer’ from the menu bar.</p>
</div>

<div class="section">
<h2 id="example_scene">Text and Choices Example Scene</h2>
<p>Narramancer includes a handful of example scenes demonstrating some basic implementations of the system. They are located in the folder Narramancer/Scenes.</p>
<p>For a simple example of printing text to the screen and offering the player choice buttons open the Text and Choices Example Scene.</p>
<div class="figure">
    <img src="/images/text_and_choices_example_scene.png" alt="Screenshot of the Text and Choices Example Scene asset; it's location in the assets folder and the hierarchy of the scene.">
    <p>A screenshot of where the Text and Choices Example Scene asset is located in the assets folder and the contents of the hierarchy of the scene.</p>
</div>
<br/>
<p>This example scene demonstrates simple text printing and choice selection. Upon entering Play Mode, the user is presented with a text dialog box which will progress when the user clicks on the screen. Eventually, the user will be presented with two choices, which will result in one of two text paths progressing.</p>
<p>The flow of this example scene is contained entirely within the ActionVerb asset named ‘Text and Choices Example Verb’. If you select the ‘Narramancer Scene’ object within the scene you will see the ActionVerb included in the list of ‘Run on Start Verbs’.</p>
</div>

<div class="section">
<h2 id="xnode">xNode</h2>
<p>Narramancer is built using a modified version of <a href="https://github.com/Siccity/xNode">xNode</a>, an open-source framework for building NodeGraph editor tools within Unity.</p>
<p>While not required, it may be beneficial to read the xNode <a href="https://github.com/Siccity/xNode/wiki/Getting%20Started">Getting Started</a> documentation to better understand some of the terms and ideas Narramancer builds off of.</p>
</div>
    
<a href="/verbs"><button class="next">Next: Verbs</button></a>