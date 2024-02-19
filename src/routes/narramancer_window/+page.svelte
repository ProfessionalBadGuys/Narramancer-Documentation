
<div class="section">
    <h2 id="window">Narramancer Window</h2>
    <p>The Narramancer Window acts as a hub for the main elements of your game, including the Verbs, the Nouns, and Global Variables.</p>
    <p><i>Advanced note: the Narramancer Window is the properties panel for Narramancer Singleton, which is a ScriptableObject.</i></p>
    <p>The window has two views: <a href="#editor_mode">Editor Mode</a> and <a href="#runtime_mode">Runtime Mode</a>.</p>
</div>

<div class="section">
    <h2 id="accessing">Accessing the Narramancer Window</h2>
    <p>To open the Narramancer Window, use the menu bar at the top of the Unity Editor, choose Window -> Narramancer.</p>
    <div class="figure">
        <img src="/images/narramancer_window_menu_item.png" alt="The menu for opening the Narramancer Window">
        <p>The menu for opening the Narramancer Window.</p>
    </div>
    <br/>
    <p>The Narramancer Window will open up as a Unity Panel, and can be docked in a way like the Inspector panel or the Project panel.</p>
</div>

<div class="section">
    <h2 id="editor_mode">Editor Mode</h2>
    <p>The Editor mode allows you to attach starting nouns and verbs, as well as assign other values.</p>
    <div class="figure">
        <img src="/images/narramancer_window_editor_mode.png" alt="A screenshot of the Narramancer Window in Editor Mode">
        <p>A screenshot of the Narramancer Window in Editor Mode.</p>
    </div>
    <br/>
    <p>Editor Mode has four subviews: Nouns, Adjectives, Verbs, and <a href="#variables">Variables</a>.</p>
    <p>The first three sub views allow you to assign the starting Nouns, Adjectives, and Verbs, respectively. Nouns applied this way will be instantiated on game start, and Verbs assigned this way will run immediately after.</p>
</div>

<div class="section">
    <h2 id="variables">Variables</h2>
    <p>Narramancer has a built-in 'variables' feature, which allows values to be assigned, accessed, and manipulated from various parts of the system.</p>
    <p>The following section outlines what we call Global Variables. There are also <a href="/components#narramancer_scene">Scene Variables</a> and <a href="/verbs#inputs_outputs">Verb Variables</a>. The three 'scopes' differ in where they exist, but are similar in how that are used.</p>
    <p>To use a variable, it must be defined prior to runtime and it must have a type and a name.</p>
    <h4>Creating Variables</h4>
    <p>Open the Narramancer window, use the Editor mode, switch to the Variables Tab, and add Variables using the variables list.</p>
    <div class="figure">
        <img src="/images/narramancer_window_variables.png" alt="A screenshot of the Variables tab within the Narramancer Window.">
        <p>A screenshot of the Variables tab within the Narramancer Window. There are two variables defined: an integer</p>
    </div>
    <br/>
    <h4>Starting Values</h4>
    <p>The third field on the variables table is for the 'starting value' (for supported types). The variable will take on this value on game start.</p>
    <h4>GameObject Starting Values</h4>
    <p>Assigning GameObjects from within a scene to a variable's starting value is not supported. In order to reference in-scene GameObjects using variables, there are three ways:</p>
    <ol>
        <li>Use a <a href="/components#setglobalvariablesmonoBehaviour">SetGlobalVariablesMonoBehaviour</a> to assign the global variable on scene start.</li>
        <li>Use a <a href="/components#narramancer_scene">Narramancer Scene</a> component and assign the desired GameObject to a Scene variable.</li>
        <li>Use a <a href="/components#runactionverbmonobehaviour">RunActionVerbMonoBehaviour</a> and assign the GameObject to a Verb variable.</li>
    </ol>
    <h4>Using Variables</h4>
    <p>Global variables are assigned using <a href="/list_nodes#setvariablenode">SetVariableNodes</a> (with the setting for scope set to Global). Note that the node can only be used in ActionVerbs and will only assign the value when it runs.</p>
    <div class="figure">
        <img src="/images/set_global_variable_node.png" alt="A SetVariableNode assigning a value to the 'money' global variable.">
        <p>A SetVariableNode assigning a value to the 'money' global variable.</p>
    </div>
    <br/>
    <p>Accessing global variables can be done using a <a href="/list_nodes#getvariablenode">GetVariableNode</a> with its scope set to Global.</p>
    <div class="figure">
        <img src="/images/get_global_variable_node.png" alt="A GetVariableNode getting the value of the 'money' global variable.">
        <p>A GetVariableNode getting the value of the 'money' global variable.</p>
    </div>
    <br/>
</div>

<div class="section">
    <h2 id="runtime_mode">Runtime Mode</h2>
    <p>During Unity Play Mode and using the Narramancer Runtime Mode, you can see the current table of NounInstances and manipulate various values.</p>
    <div class="figure">
        <img src="/images/narramancer_window_runtime_mode.png" alt="A screenshot of the Narramancer Window in Runtime Mode">
        <p>A screenshot of the Narramancer Window in Runtime Mode.</p>
    </div>
    <br/>
    <p>For debuging or testing purposes, you can see all aspects of each NounInstance, as well as add or remove properties and stats.</p>
</div>

<div class="section">
    <h2 id="singleton">Singleton</h2>
    <p>The Narramancer system uses a Singleton pattern, meaning there is one static class (called an instance, not to be confused with NounInstances) that handles most of the functionality. The Narramancer Singleton is guaranteed to exist at game start because it is a ScriptableObject asset.</p>
    <p>Script and code can call almost any Narramancer method using a static call to NarramancerSingleton.Instance.</p>
    <div class="figure">
        <img src="/images/narramancer_singleton_instance.png" alt="A code example of accessing the NarramancerSingleton instace.">
        <p>A snippet of code with two uses of the NarramancerSingleton instance: the first one attempts to get a NounInstance, and the second one creates a new NounInstace.</p>
    </div>
    <br/>
    <p>This allows you to have access to the table of nouns as well as other functionality.</p>
    <p>The Narramancer Window is (more or less) the properties of the Narramancer Singleton ScriptableObject.</p>
</div>

<a href="/saving_loading"><button class="next">Next: Saving and Loading</button></a>
