
<div class="section">
    <h2 id="verb_editor">Verb Editor</h2>
    <p>The most useful tool of Narramancer is the NodeGraph editor used to manipulate verbs.</p>
    <p>To open the NodeGraph editor window, double click on any Verb asset (ValueVerb or ActionVerb) OR select a Verb asset and click on ‘Edit Graph’ in the asset’s inspector.</p>
    <div class="figure">
        <img src="/images/verb_editor.png" alt="Screenshot of the Narramancer Verb Editor.">
        <p>A screenshot of the Narramancer Verb Editor</p>
    </div>
</div>

<div class="section">
    <h2 id="basic_controls">Basic Controls</h2>
    <table>
        <tr>
          <th>Input</th>
          <th>Effect</th>
        </tr>
        <tr>
          <td>Mouse Scroll</td>
          <td>Zoom In and Zoom Out</td>
        </tr>
        <tr>
        <td>Press Middle Mouse Button and Drag</td>
        <td>Pan Visible Area</td>
        </tr>
        <tr>
            <td>Press F Key</td>
            <td>Jump to the ‘origin’ of the visible area</td>
        </tr>
        <tr>
            <td>Click Left Mouse Button</td>
            <td>Select a Node</td>
        </tr>
        <tr>
            <td>Press Left Mouse Button on an empty area and Drag</td>
            <td>Start a Selection Box, selecting all encompassed Nodes</td>
        </tr>
        <tr>
            <td>Press Left Mouse Button on a node and Drag</td>
            <td>Drag or translate the selected node or nodes</td>
        </tr>
        <tr>
            <td>Press Left Mouse Button on a node’s output port and Drag, releasing on another node’s input port</td>
            <td>Create a connection between the two nodes by the given ports</td>
        </tr>
        <tr>
            <td>Click Right Mouse Button in Empty Area</td>
            <td>Open the Create Node Context Menu</td>
        </tr>
        <tr>
            <td>Click Right Mouse Button on a Node</td>
            <td>Open the Node Context Menu</td>
        </tr>
    </table>
</div>

<div class="section">
    <h2 id="create_node_context_menu">Create Node Context Menu</h2>
    <p>The Node Context Menu allows you to create and add new nodes to the given graph at the given position.</p>
    <div class="figure">
        <img src="/images/node_context_window.png" alt="Screenshot of the Node Context Window.">
        <p>The Node Context Window, which creates new nodes in the given Verb.</p>
    </div>
    <br/>
    <p>The various possible nodes are organized by their function.</p>
    <h4>Search Nodes Window</h4>
    <p>To find a given node quickly, choose the ‘Search…’ option from the Create Node Context Menu and use the Node Search Dialog to find the node by name.</p>
    <div class="figure">
        <img src="/images/search_node_dialog_window.png" alt="Screenshot of the Node Search Window.">
        <p>A screenshot of the Node Search Window, where you can search for a specific node by typing in its name.</p>
    </div>
    <br/>
</div>

<div class="section">
    <h2 id="creating_nodes">Creating Nodes</h2>
    <p>To add a new Node to a Verb, right-click within an empty area of the Verb Editor to open the Create Node Context Menu. From the context menu, either 'Search' for the node by name or find the node within the hierarchy.</p>
    <div class="figure">
        <img src="/images/create_new_node.gif" alt="Demonstration of creating a new node in the Verb Editor">
        <p>A demonstration of creating a new node.</p>
    </div>
    <br/>
    <p>Selecting the node type will create the given node at the given location.</p>
</div>

<div class="section">
    <h2 id="connecting_nodes">Connecting Nodes</h2>
    <p>In order to create chains of actions, you must connect them to each other.</p>
    <p>Nodes that are ‘runnable’ have two special ports: one input port referred to as ‘This Node’ that causes the node to ‘run’ and one output port that, upon completing its own run, triggers the next runnable node to run. These special ports have triangle/arrow shapes to help differentiate them.</p>
    <p>To create a chain of runnable nodes, click and drag off of the output port of the first and drop it on the input port of the second.</p>
    <div class="figure">
        <img src="/images/connect_nodes.gif" alt="Demonstration of connecting two nodes in the Verb Editor">
        <p>A demonstration of connecting two nodes.</p>
    </div>
    <br/>
    <p>For nodes that have input and output ports, the process of connecting them is the same. NOTE: ports can only be connected if they are of the same type.</p>
</div>

<a href="/list_nodes"><button class="next">Next: A List of All Node Types</button></a>