
<div class="section">
    <h2 id="verbs">Verbs</h2>
    <p>A graph of nodes is called a Verb in Narramancer. Verb assets extend from Unity ScriptableObjects and exist as individual files within the project folder.</p>
    <p>Verbs can also have inputs and outputs, which allow values of various types to be passed in and/or returned out.</p>
    <p>Verbs come in two types: ValueVerbs and ActionVerbs.</p>
</div>

<div class="section">
    <h2 id="action_verbs">Action Verbs</h2>
    <p>Verbs that perform actions over realtime are called ActionVerbs.</p>
    <p>ActionVerbs have access to a category of nodes referred to as RunnableNodes.</p>
    <p>Depending on the nodes that they are made of, an ActionVerb may execute and complete instantatiously, take several seconds or minutes, or run until the player enters some kind of input.</p>
</div>

<div class="section">
    <h2 id="action_verbs">Value Verbs</h2>
    <p>Verbs that strictly get information are called ValueVerbs.</p>
    <p>ValueVerbs don't run or execute in the same way that ActionVerbs do. They cannot use RunnableNodes, but still have access to all other basic nodes.</p>
</div>

<div class="section">
    <h2 id="creating_verbs">Creating Verbs</h2>
    <p>There are two main ways to create new Verbs:</p>
    <ol>
        <li>
            Right-click anywhere in the project and use the Asset Creation menu to create a new verb asset, either a ValueVerb OR and ActionVerb from under the Narramancer menu.
        </li>
        <li>
            Create and add an ActionVerb to a Narramancer Scene component by using the plus button and selecting ‘Create new asset’:
        </li>
    </ol>
</div>

<div class="section">
    <h2 id="running_verbs">Running Verbs</h2>
    <p>Verbs will not run unless they are attached to a NodeRunner. To attach an ActionVerb to a NodeRunner, either:</p>
    <ol>
        <li>
            Right-click anywhere in the project and use the Asset Creation menu to create a new verb asset, either a ValueVerb OR and ActionVerb from under the Narramancer menu.
        </li>
        <li>
            Create and add an ActionVerb to a Narramancer Scene component by using the plus button and selecting ‘Create new asset’.
        </li>
    </ol>
</div>

<a href="/verb_editor"><button class="next">Next: Verb Editor</button></a>