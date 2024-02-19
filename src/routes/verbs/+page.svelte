
<div class="section">
    <h2 id="verbs">Verbs</h2>
    <p>A graph of nodes is called a Verb in Narramancer. Verb assets extend from Unity ScriptableObjects and exist as individual files within the project folder.</p>
    <p>Verbs can also have inputs and outputs, which allow values of various types to be passed in and/or returned out.</p>
    <p>Verbs come in two types: <a href="#value_verbs">ValueVerbs</a> and <a href="#action_verbs">ActionVerbs</a>.</p>
</div>

<div class="section">
    <h2 id="action_verbs">Action Verbs</h2>
    <p>Verbs that perform actions over time are called ActionVerbs.</p>
    <p>ActionVerbs have access to a category of nodes referred to as RunnableNodes.</p>
    <p>Depending on the nodes that they are made of, an ActionVerb may execute and complete instantaneously, take several seconds or minutes, or run until the player enters some kind of input.</p>
    <p>ActionVerbs must have exactly one RootNode, which connects to one RunnableNode and tells the verb which node to run first.</p>
</div>

<div class="section">
    <h2 id="value_verbs">Value Verbs</h2>
    <p>Verbs that strictly get information are called ValueVerbs.</p>
    <p>ValueVerbs don't run or execute in the same way that ActionVerbs do. They cannot use RunnableNodes, but still have access to all other basic nodes.</p>
</div>

<div class="section">
    <h2 id="within_verbs">Verbs Within Verbs</h2>
    <p>One powerful feature of Verbs is their ability to run other verbs.</p>
    <p>By using either the RunActionVerbNode or the RunValueVerbNode, the effects or outputs of one verb can be used within another.</p>
    <p>NOTE: ActionVerbs can use ValueVerbs, but ValueVerbs <strong>cannot</strong> use ActionVerbs.</p>
</div>

<div class="section">
    <h2 id="creating_verbs">Creating Verbs</h2>
    <p>There are two main ways to create new Verbs:</p>
    <ol>
        <li>
            Right-click anywhere in the project and use the Asset Creation menu to create a new verb asset, either a ValueVerb OR an ActionVerb from under the Narramancer menu.
        </li>
        <li>
            Create and add an ActionVerb to a Narramancer Scene component by using the plus button and selecting ‘Create new asset’:
        </li>
    </ol>
</div>

<div class="section">
    <h2 id="running_verbs">Running Verbs</h2>
    <p>Verbs will not run during your game unless they are attached to a NodeRunner. To attach an ActionVerb to a NodeRunner, either:</p>
    <ol>
        <li>
            <p>Open the Narramancer Window, navigate to the 'Verbs' tab, and add the ActionVerb to the list of 'Run At Start' verbs either by dragging and dropping the asset there or by using the plus button and selecting 'Add Existing...'</p>
            <p>ActionVerbs in the Narramancer Window will run immediately at the start of the game.</p>
        </li>
        <li>
            <p>Add the ActionVerb to a Narramancer Scene component by either dragging and dropping the asset on the 'Run On Start Verbs' list or by using the plus button and selecting 'Add Existing...'</p>
            <p>ActionVerbs attached to a Narramancer Scene will run when the scene is loaded and started.</p>
        </li>
    </ol>
</div>

<div class="section">
    <h2 id="inputs_outputs">Verb Inputs and Outputs</h2>
    <p>Verbs can have input values and output values. Not be be confused with Node input and outpus, Verb inputs and outputs can be defined by the developer.</p>
    <p>Input and output values are particularly useful when using ValueVerbs within other verbs: various arguments can be passed in to the ValueVerb as parameters, the logic of the ValueVerb executes, and the ValueVerb provides one or more values as outputs.</p>
    <p>To add or edit a verb's inputs and outputs, select the verb asset and access the Inspector Window.</p>
    <div class="figure">
        <img src="/images/verb_inputs_and_outputs.png" alt="A Verb asset Inspector Window with Inputs and Outputs.">
        <p>A Verb asset Inspector Window with Inputs and Outputs.</p>
    </div>
    <br/>
    <p>Use the plus button on either the input list or the output list to create an input or an output respectively. You must assign what type the input/output is and you must give it a unique name.</p>
    <p>Outputs for ValueVerbs are assigned using <a href="/list_nodes#outputnode">OutputNodes</a>.</p>
    <div class="figure">
        <img src="/images/output_node.png" alt="An OutputNode with an output named 'Result'.">
        <p>An OutputNode with an output named 'Result'.</p>
    </div>
    <br/>
    <p>Outputs for ActionVerbs are assigned using <a href="/list_nodes#setvariablenode">SetVariableNodes</a> with its scope set to Verb. Note that the node will only assign the value to the output variable when it executes.</p>
    <div class="figure">
        <img src="/images/set_variable_node.png" alt="A SetVariableNode assigning a value to the 'Result' variable.">
        <p>A SetVariableNode assigning a value to the 'Result' variable.</p>
    </div>
    <br/>
    <p>Accessing verb input values is the same for ActionVerbs and ValueVerbs and uses a <a href="/list_nodes#getvariablenode">GetVariableNode</a> with its scope set to Verb.</p>
    <div class="figure">
        <img src="/images/get_variable_node.png" alt="A GetVariableNode getting the value of the 'Result' variable.">
        <p>A GetVariableNode getting the value of the 'Result' variable.</p>
    </div>
    <br/>
</div>

<a href="/verb_editor"><button class="next">Next: Verb Editor</button></a>