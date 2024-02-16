
<div class="section">
    <h2 id="all_nodes">List of all Nodes</h2>
    <p>Here you will find an alphabetical list of all Narramancer nodes. We give a brief description of the node as well as its inputs and outputs. There are roughly 130 concrete nodes.</p>
    <p>Please use search functionality or the directory on the right to jump to the node you are looking for.</p>
</div>

<div class="section">
    <h2 id="choicenode">ChoiceNode</h2>
    <p>A companion to the <a href="#offerchoicesnode">OfferChoicesNode</a>, the ChoiceNode represents a single choice that can be offered to the player.</p>
    <div class="figure">
        <img src="/images/offer_choices_and_choice_nodes.png" alt="A screenshot of an OfferChoicesNode and two connected ChoiceNodes.">
        <p>A screenshot of an OfferChoicesNode and two connected ChoiceNodes.</p>
    </div>
    <br/>
    <p>The RunnableNode connected to the Choice Node that is selected by the player is the one that will then be run by the system.</p>
    <p>The Choice Node has various options that affect how it is displayed. If Enabled is set to false then the option will not be displayed at all UNLESS Display When Disabled is set to true, in which case it will be displayed but in a disabled style.</p>
</div>

<div class="section">
    <h2 id="offerchoicesnode">OfferChoicesNode</h2>
    <p>The OfferChoicesNode displays any connected <a href="#choicenode">ChoiceNodes</a> to the player as buttons and waits for them to select one.</p>
    <div class="figure">
        <img src="/images/offer_choices_and_choice_nodes.png" alt="A screenshot of an OfferChoicesNode and two connected ChoiceNodes.">
        <p>A screenshot of an OfferChoicesNode and two connected ChoiceNodes.</p>
    </div>
    <br/>
    <p>The Offer Choices Node can have any number of Choice Nodes connected to it.</p>
</div>

<div class="section">
    <h2 id="printtextnode">PrintTextNode</h2>
    <p>The Print Text Node is a RunnableNode that will display narrative text to the player.</p>
    <div class="figure">
        <img src="/images/print_text_node.png" alt="A screenshot of a PrintTextNode.">
        <p>A screenshot of a PrintTextNode.</p>
    </div>
    <br/>
    <p>The text can either be typed into the text editor field OR given as an input by connecting the text input port.</p>
    <p>A Text Printer can also be given, which will determine the GameObject that receives the text, but if none is set then the first one found in the scene will be used.</p>
    <p>The text editor field supports rich text tags, and provides convenience buttons for added tags around selected text. The R button will enable or disable the rich text being displayed in the editor. The B button will add (or remove) bold tags around the selected text. The I button will add (or remove) italic tags around the selected text. The C button will add (or remove) color tags for the color currently selected by the color picker around the selected text.</p>
    <p>The Print Text Node can also be <strong>resized</strong> by selecting the node and dragging the bottom right corner.</p>
    <p>The Print Text Node also allows for dynamic terms within the text using inputs. Use the ‘Add New Input’ button to create an input for any given type. Give the input a name, then use that name wrapped in curly brackets within the text to have that term replaced with the string representation of the input value.</p>
    <div class="figure">
        <img src="/images/print_text_node_with_input.png" alt="A PrintTextNode with one dynamic input.">
        <p>A PrintTextNode with one dynamic input named 'characterName'.</p>
    </div>
    <br/>
    <p>The example given in the above figure will result in the text output to be <i>“Hello, Samuel!” He said.</i></p>
</div>

<a href="/nouns"><button class="next">Next: Nouns</button></a>