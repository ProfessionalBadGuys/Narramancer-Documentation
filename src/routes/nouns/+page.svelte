<div class="section">
    <h2 id="nouns">Nouns</h2>
    <p>In addition to handling game logic flow, Narramancer provides a general-purpose table of the 'things' in your game.</p>
    <p>These things may or may not be associated with GameObjects, especially as scenes are unloaded and changed, but the game needs some way of remembering them. The various things in your game may include characters, equipment, items, or areas.</p>
    <p>The Narramancer system makes no assumptions about what your things are and refers to them simply as <strong>Nouns</strong>. Nouns are simply named containers with no inherent value <strong>until</strong> they are attached with developer-defined <a href="#adjectives">adjectives</a>.</p>
    <p>Structuring the characters and items in your game as Narramancer Nouns has two distinct advantages:</p>
    <ol>
        <li>
            Nouns and anything attached to them automatically get saved and loaded as part of the game state.
        </li>
        <li>
            Nouns are easy to query and manipulate within Verbs through various noun-specific nodes.
        </li>
    </ol>
    <p>Nouns and adjectives are defined using ScriptableObjects.</p>
</div>

<div class="section">
    <h2 id="creating_nouns">Creating New Nouns</h2>
    <h4>Method 1</h4>
    <p>Use the Narramancer Window; open it to the Editor -> Nouns tab, and use the plus button.</p>
    <div class="figure">
        <img src="/images/narramancer_window_create_new_noun.png" alt="Demonstration of creating a new noun using the Narramancer Window">
        <p>A demonstration of creating a new noun using the Narramancer Window.</p>
    </div>
    <br/>
    <p>This will open a save prompt, allowing you to choose a location and a name for the new Noun asset.</p>
    <p>This will also add the Noun asset to Narramancer's global list of Nouns. Nouns that Narramancer does NOT know about will not get created at runtime.</p>
    <h4>Method 2</h4>
    <p>Nouns can also be created from the Asset Creation Menu by right-clicking somewhere in the project, and then choosing Create -> Narramancer -> Noun from the context menu. This will create a Noun Asset at the given location but will NOT automatically add the Noun to Narramancer's global list of Nouns.</p>
    <h4>Method 3</h4>
    <p>Nouns do not necessarily need to be associated with an asset (ie: NounScriptableObject).</p>
    <p>You can create nouns at runtime using ActionVerbs and the CreateNounNode. Nouns created this way are automatically registered with the Narramancer table.</p>
</div>

<div class="section">
    <h2 id="instances">Instances</h2>
    <p>An important distinction to make is between a NounScriptableObject and a NounInstance.</p>
    <p>A NounScriptableObject exists as an asset prior to the game starting and is used to create a NounInstance. The values of a NounScriptableObject represent the Noun's <strong>starting values and qualities</strong>, but changes made to the NounInstance during runtime are <strong>not</strong> applied to the NounScriptableObject and vice-versa.</p>
    <p>A NounInstance represents a mutable Noun object and exists only while the game is running. It may have been created from a NounScriptableObject (ie: if it was created using Methods 1 or 2) but not necessarily (as is the case if it was created using Method 3).</p>
    <p>That being said, NounScriptableObjects can be used to find their corresponding NounInstance by using a GetInstanceNode.</p>
    <p>Within verbs and nodes, Nouns and NounInstances are typically referred to as just Instances.</p>
</div>

<div class="section">
    <h2 id="adjectives">Adjectives</h2>
    <p>Nouns gain their value by the adjectives attached to them. In Narramancer, we use the term 'adjective' to describe components or pieces that can be added to a Noun.</p>
    <p>It is up to you to define the various adjectives in your game by creating the various assets/ScriptableObjects associated with them.</p>
    <p>The three types of adjectives are: <a href="#properties">Properties</a>, <a href="#stats">Stats</a>, and <a href="#relationships">Relationships</a>.</p>
    <p>Similar to nouns, adjectives are defined using ScriptableObjects, then instances of each adjective are created during runtime.</p>
</div>

<div class="section">
    <h2 id="properties">Properties</h2>
    <p>A Property is a named quality that can be attached to a Noun and used to identify that noun as being part of a group or flag a noun as having a certain quality or being treated in a certain way.</p>
</div>

<div class="section">
    <h2 id="stats">Stats</h2>
    <p>Stats are number values that can be attached to a noun, then modified over the course of the game. You can use stats to represent a noun's health, mana, strength, or even as a running count of how many battles this noun has been in.</p>
    <div class="figure">
        <img src="/images/stat_inspector_window.png" alt="A screenshot of a StatScriptableObject Inspector window">
        <p>A screenshot of a StatScriptableObject Inspector window.</p>
    </div>
    <br/>
    <p>Each stat can have an optional min value, max value, or starting value that will affect its behavior over the course of the game.</p>
</div>

<div class="section">
    <h2 id="relationships">Relationships</h2>
    <p>Relationships are unidirectional connections between two nouns. They can be added or removed over the course of the game, and are useful ways to represent things like how characters are related (eg: siblings), what has happened in the history between two characters, or how two areas are connected to each other.</p>
    <p>Relationships are decidedly <strong>unidirectional</strong>, meaning the relationship only applies one way. We designate this by saying that one entity is the source of the relationship and one entity is the destination. This becomes important when using queries to find nouns based on these relationships.</p>
</div>

<div class="section">
    <h2 id="creating_adjectives">Creating Adjectives</h2>
    <h4>Method 1</h4>
    <p>Use the Narramancer Window; open it to the Editor -> Adjective tab, and use the "Create new" button, then choose one of the types.</p>
    <div class="figure">
        <img src="/images/narramancer_window_create_new_adjective.png" alt="Demonstration of creating a new adjective using the Narramancer Window">
        <p>A demonstration of creating a new adjective using the Narramancer Window.</p>
    </div>
    <br/>
    <p>This will open a save prompt, allowing you to choose a location and a name for the new Adjective asset.</p>
    <h4>Method 2</h4>
    <p>Adjectives can also be created from the Asset Creation Menu by right-clicking somewhere in the project, and then choosing Create -> Narramancer -> Property/Stat/or Relationship from the context menu. This will create the given adjective asset at the given location.</p>
</div>

<div class="section">
    <h2 id="attaching_adjectives">Attaching Starting Adjectives to Nouns</h2>
    <p>In order to attach properties, stats, or relationships to a noun, simply select the NounScriptableObject and add the adjective to its corresponding list.</p>
    <div class="figure">
        <img src="/images/character_starting_adjectives.png" alt="A screenshot of a noun and its inspector window, with starting adjectives added.">
        <p>A screenshot of a noun and its inspector window, with starting adjectives added.</p>
    </div>
    <br/>
    <p>Properties, stats, and relationships added this way will be automatically initialized on the given noun on game start.</p>
    <p>For stats, be sure to assign a starting value.</p>
    <p>For relationships, be sure to assign the other noun in the relationship, and determine whether this noun is the source of the relationship or the destination.</p>
</div>

<div class="section">
    <h2 id="nouns_example_scene">Example Scene: Creating and Destroying Nouns</h2>
    <p>We have provided an example scene demonstrating basic noun creation as well as destruction during runtime using ActionVerbs.</p>
    <div class="figure">
        <img src="/images/noun_creation_example_scene.png" alt="A screenshot of where to find the Noun Creation and Destruction Scene asset.">
        <p>A screenshot of where to find the Noun Creation and Destruction Scene asset.</p>
    </div>
    <br/>
    <p>Opening and playing this scene will present the player with a series of looping choices, allowing them to continuously create and destroy nouns.</p>
    <p>Open the associated ActionVerb (Noun Creation and Destruction Verb.asset) in the Verb Editor to see the entire flow of logic.</p>
    <p>The nodes of note are the CreateInstanceNode and the DestroyInstanceNode.</p>
</div>

<div class="section">
    <h2 id="properties_example_scene">Example Scene: Adding and Removing Properties</h2>
    <p>We have provided an example scene demonstrating basic noun creation as well as destruction during runtime using ActionVerbs.</p>
    <div class="figure">
        <img src="/images/add_properties_example_scene.png" alt="A screenshot of where to find the Adding and Removing Properties Scene asset.">
        <p>A screenshot of where to find the Adding and Removing Properties Scene asset.</p>
    </div>
    <br/>
    <p>Opening and playing this scene will present the player with a series of looping choices, allowing them to continuously create and destroy nouns.</p>
    <p>Open the associated ActionVerb (Noun Creation and Destruction Verb.asset) in the Verb Editor to see the entire flow of logic.</p>
    <p>The nodes of note are the CreateInstanceNode and the DestroyInstanceNode.</p>
</div>

<a href="/getting_started"><button class="next">Next: Getting Started</button></a>