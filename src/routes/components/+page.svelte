<div class="section">
    <h2 id="narramancer_scene">Narramancer Scene</h2>
    <p>A Narramancer Scene component can be added to a scene to tell the Narramancer system key aspects about the given scene. Only one Narramancer Scene component at most should exist in a scene.</p>
    <p>The three main parts of the Narramancer Scene are a list of Nouns, a list of Variables, and a list of ActionVerbs.</p>
    <p>When the scene starts:</p>
    <ol>
        <li>The given Nouns will be created/initialized and added to the table.</li>
        <li>The Scene Variables will be assigned to their corresponding starting values.</li>
        <li>Any ActionVerbs in the list are run.</li>
    </ol>
    <p>A Narramancer Scene component can be added to a GameObject OR a whole Narramancer Scene GameObject can be created using the create new GameObject context menu, found under Narramancer -> Narramancer Scene.</p>
</div>

<div class="section">
    <h2 id="textprinter">TextPrinter</h2>
    <p>A TextPrinter is a component that displays narrative text to the player, usually using a revealing animation. TextPrinters are required to use <a href="/list_nodes#printtextnode">PrintTextNodes</a>. A prefab for a ready-to-go TextPrinter GameObject is provided in the folder /Narramancer/Prefabs/.</p>
</div>

<div class="section">
    <h2 id="choiceprinter">ChoicePrinter</h2>
    <p>A ChoicePrinter is a component that displays choices as buttons to the player. A ChoicePrinter is required to use <a href="/list_nodes#offerchoicesnode">OfferChoicesNode</a>. A prefab for a ready-to-go ChoicePrinter GameObject is provided in the folder /Narramancer/Prefabs/.</p>
</div>

<div class="section">
    <h2 id="textandchoiceprinter">TextAndChoicePrinter</h2>
    <p>TextAndChoicePrinter combines the functionality of a TextPrinter and a ChoicePrinter into one interface, allowing text and choices to exist in the same ScrollView. A prefab for a ready-to-go TextAndChoicePrinter GameObject is provided in the folder /Narramancer/Prefabs/ and this is the one that is used in all Narramancer Example scenes.</p>
</div>

<div class="section">
    <h2 id="save_menu">SaveMenu</h2>
    <p>The SaveMenu component handles the menu and functionality that allows the player to save their game. A prefab for a ready-to-go SaveMenu GameObject is provided in the folder /Narramancer/Prefabs/ and this is the one that is used in all Narramancer Example scenes.</p>
</div>

<div class="section">
    <h2 id="load_menu">LoadMenu</h2>
    <p>The LoadMenu component handles the menu and functionality that allows the player to load a saved game. A prefab for a ready-to-go LoadMenu GameObject is provided in the folder /Narramancer/Prefabs/ and this is the one that is used in all Narramancer Example scenes.</p>
</div>

<div class="section">
    <h2 id="spawner">SerializableSpawner</h2>
    <p>A SerializableSpawner is a component that spawns other GameObjects. The type of GameObject spawned is defined by a single predefined GameObject or Prefab. Various settings are provided for where the new spawned object is created. Spawners are required to use <a href="/list_nodes#spawnnode">SpawnNodes</a> and can also be used by <a href="/list_nodes#createinstancenode">CreateInstanceNode</a>. GameObjects created and handled by SerializableSpawners will automatically be saved and recreated on load.</p>
    <p>A SerializableSpawner component can be added to a GameObject OR a whole SerializableSpawner GameObject can be created using the create new GameObject context menu, found under Narramancer -> Serializable Spawner.</p>
</div>

<div class="section">
    <h2 id="runactionverbmonobehaviour">RunActionVerbMonoBehaviour</h2>
    <p>Use a RunActionVerbMonoBehaviour to run an ActionVerb on scene load (or triggered by other things such as UnityEvents). This component also allows for verb input values to be assigned using a list of assignments. Input values that are components or GameObjects can be assigned to in-scene objects.</p>
    <p>To control when the ActionVerb runs, you can disable 'Run on Start' and call the public method RunVerb() on the component instead.</p>
    <p>A RunActionVerbMonoBehaviour component can be added to a GameObject OR a whole RunActionVerbMonoBehaviour GameObject can be created using the create new GameObject context menu, found under Narramancer -> Run Action Verb.</p>
</div>

<div class="section">
    <h2 id="setglobalvariablesmonobehaviour">SetGlobalVariablesMonoBehaviour</h2>
    <p>Use a SetGlobalVariablesMonoBehaviour to assign values to Global Variables on scene start (or triggered by other things such as UnityEvents). This is the only way to use in-scene components and GameObjects as values for Global Variables.</p>
    <p>To control when the values are assigned, you can disable 'Run on Start' and call the public method ApplyValues() on the component instead.</p>
    <p>A SetGlobalVariablesMonoBehaviour component can be added to a GameObject OR a whole SetGlobalVariablesMonoBehaviour GameObject can be created using the create new GameObject context menu, found under Narramancer -> Set Global Variables.</p>
</div>

<div class="section">
    <h2 id="createnounforgameobject">CreateNounForGameObject</h2>
    <p>Using a CreateNounForGameObject is <a href="/nouns#creating_nouns">one way of creating NounInstances</a> within your game. This method is similar to defining a noun using NounScriptableObjects, but is preferred if your nouns are highly coupled to GameObjects. Creating a noun using this component automatically connects the new NounInstance with the attached GameObject, which will be saved and recreated on load.</p>
</div>
    
<div class="section">
    <h2 id="overview">SetEnabledFromProperty</h2>
    <p>The SetEnabledFromProperty is a simple way of activating or disabled a given GameObject based on if a given Noun currently has a given property.</p>
    <p>NOTE that the target GameObject being enabled and disabled should NOT be the same one that has this component, as the update functionality will stop working when the GameObject first gets disabled.</p>
</div>

<div class="section">
    <h2 id="overview">SetSliderFromStat</h2>
    <p>The SetSliderFromStat is a simple way of reflecting a given Noun's stat value using a Unity.UI.Slider. The component can be attached to a Slider, and will continuously apply the current value of the noun's stat.</p>
</div>

<a href="/flags"><button class="next">Next: Flags</button></a>