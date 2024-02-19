
<div class="section">
    <h2 id="nodes">Nodes</h2>
    <p>The basic building blocks of Narramancer are the nodes.</p>
    <div class="figure">
        <img src="/images/graph_of_nodes.png" alt="A graph of connected nodes within an ActionVerb.">
        <p>A graph of connected nodes.</p>
    </div>
    <br/>
    <p>ActionVerbs and ValueVerbs have little value without nodes. Each node has a specific function, whether it is to get a value and pass it along, or to execute a certain task such as arithmetic or GameObject manipulation. </p>
</div>

<div class="section">
    <h2 id="node_ports">Node Ports</h2>
    <p>Nodes have one or more ports which allow values to be exchanged or assigned. Ports are either inputs into the node (and appear on the left side of the node) or outputs from the node (appearing on the right side).</p>
    <p>Nodes are connected to one another via these ports: input to output. Input ports (usually) can only be connected to one output port at a time, but output ports can (usually) be connected to multiple input ports. </p>
    <p>Ports are <strong>typed</strong>, and by that we mean that the value of a port is predefined and corresponds to a C# class, either numbers, strings, Lists, etc. Ports can only be connected to each other if they are of the same type (or at least compatible).</p>
    <p>Input ports that are primitive values, such as ints, floats, or strings, usually allow for a default value to be assigned using the inspector.</p>
    <div class="figure">
        <img src="/images/node_default_inputs.png" alt="A visualization of Input Ports on a Node, specifically inputs that can be assigned default values.">
        <p>A visualization of input ports on a Node, specifically inputs that can be assigned default values.</p>
    </div>
    <br/>
    <p>In the above image, the 'Enabled' input port is a bool and will take the value 'true' because the port is unconnected and the toggle is checked. The same can be said about the 'Display Text' port: the display text can be assigned either by connecting something to the port OR by typing text into the input text field.</p>
</div>

<div class="section">
    <h2 id="runnablenodes">Runnable Nodes</h2>
    <p>RunnableNodes are a sub category of nodes that 'run' or trigger some action during the game. An action may complete instantaneously, it may take several seconds or minutes, or it may wait until a certain condition is met before completing (eg: the player presses a button).</p>
    <p>When RunnableNodes are chained together, they are executed from left to right, with each one completing before the next one starts. In this sense, a RunnableNode is similar to a state within a state machine.</p>
    <p>RunnableNodes are <strong>only</strong> usable by ActionVerbs (not by ValueVerbs).</p>
    <p>Runnable nodes (typically) have two special ports that are used to chain them together in a runnable sequence: one input port that is labeled 'This Node' and one output port labeled 'Then Run Node'. These special ports have triangle/arrow shapes to help differentiate them.</p>
    <div class="figure">
        <img src="/images/print_text_node_header.png" alt="A RunnableNode, showing the special runnable ports.">
        <p>An example of a RunnableNode (a PrintTextNode) showing the special runnable ports.</p>
    </div>
    <br/>
    <p>The first RunnableNode in an ActionVerb to be executed is the one connected to the Verb's RootNode.</p>
</div>

<div class="section">
    <h2 id="dynamically_typed">Dynamicly Typed Node Ports</h2>
    <p>Some nodes can handle various types and use a dynamicly typed port system. The node, initally, does not have ports, but once you tell it what type to use using the dropdown, the ports will be dynamically created.</p>
</div>

<div class="section">
    <h2 id="dynamically_typed">Pass-Through Values</h2>
    <p>A lot of nodes, especially those that do work on NounInstances, will pass input values through and offer them as output values. This is a convience, allowing 'down stream' nodes to connect and use those same values without the noodles crossing or growing too long.</p>
</div>

<a href="/list_nodes"><button class="next">Next: List of All Nodes</button></a>