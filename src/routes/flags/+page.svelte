<div class="section">
    <h2 id="flags">Flags</h2>
    <p>One convenience feature included with Narramancer is the Flag System.</p>
    <p>A Flag in Narramancer is simply a True or False value stored on the table.</p>
    <p>A flag can represent whether the player has seen a key part of the story yet or a key event has happened. If a flag is <a href="#raised">raised</a> then we consider that event has having happened.</p>
    <p>Each possible flag must be defined using a Flag ScriptableObject, created somewhere in the project folder using the Create Asset Context menu: Narramancer -> Flag.</p>
    <h4>Why not just use global variables?</h4>
    <p>Using global variables or other ways of keeping track of what part of the story we are in is entirely possible, but can become unwieldy if the number of events grows large. Flags provide a scalable way of having a lot of events, and referring to them using Object Fields avoids 'magic string' issues.</p>
</div>

<div class="section">
    <h2 id="raised_flags">Raised Flags</h2>
    <p>The value behind a flag is actually an integer. The value of the flag starts at zero (unless otherwise assigned) and raising a flag increments the value by one.</p>
    <p>The flag is considered <strong>raised</strong> if its value is greater than or equal to one. A flag can be raised multiple times, which can then be used to indicate not just that the event has happened at all, but count the number of times.</p>
    <p>A flag can be <strong>lowered</strong> by setting its value to zero.</p>
</div>

<div class="section">
    <h2 id="using_flags">Using Flags</h2>
    <p>The nodes used to access and manipulate flags are as follows:</p>
    <ul>
        <li>Use the <a href="/list_nodes#raiseflagnode">RaiseFlagNode</a>, <a href="/list_nodes#removeflagnode">RemoveFlagNode</a>, and <a href="/list_nodes#setflagnode">SetFlagNode</a> to raise, lower, or manually set the given flag.</li>
        <div class="figure">
            <img src="/images/runnable_flag_nodes.png" alt="A screenshot of RaiseFlagNode, RemoveFlagNode, and SetFlagNode.">
            <p>A screenshot of RaiseFlagNode, RemoveFlagNode, and SetFlagNode.</p>
        </div>
        <br/>
        <li>Use the <a href="/list_nodes#isflagraisednode">IsFlagRaisedNode</a> to check, true or false, whether a flag is raised, and the <a href="/list_nodes#getflagnode">GetFlagNode</a> to access the integer manually.</li>
        <div class="figure">
            <img src="/images/get_flag_nodes.png" alt="A screenshot of IsFlagRaisedNode and GetFlagNode.">
            <p>A screenshot of IsFlagRaisedNode and GetFlagNode.</p>
        </div>
        <br/>
    </ul>
</div>

<!-- <a href="/getting_started"><button class="next">Next: Getting Started</button></a> -->