
<div class="section">
    <h2 id="all_nodes">List of all Nodes</h2>
    <p>Here you will find an alphabetical list of all Narramancer nodes. We give a brief description of the node as well as its inputs and outputs. There are roughly 130 concrete nodes.</p>
    <p>Please use search functionality or the directory on the right to jump to the node you are looking for.</p>
    <p>If you're just getting started, you should skip this section for now and learn about <a href="/nouns">Nouns</a> next.</p>
</div>

<div class="section">
    <h2 id="frequently_use_nodes">Frequently Used Nodes</h2>
    <ul>
        <li><a href="#getinstancesnode">GetInstancesNode</a></li>
        <li><a href="#offerchoicesnode">OfferChoicesNode</a></li>
        <li><a href="#printtextnode">PrintTextNode</a></li>
        <li><a href="#runactionverbnode">RunActionVerbNode</a></li>
        <li><a href="#runvalueverbnode">RunValueVerbNode</a></li>
    </ul>
</div>


    <div class="section">
        <h2 id="addpropertiesnode">AddPropertiesNode</h2>
        <p>The AddPropertiesNode is used to add a property or properties to a noun instance. It can accept a list of properties and/or multiple property inputs.</p>
    </div>
    

    <div class="section">
        <h2 id="addrelationshipnode">AddRelationshipNode</h2>
        <p>The AddRelationshipNode is used to create relationships between instances. It takes two instances, a relationship, and a designation for which one is the source or destination.</p>
    </div>
    

    <div class="section">
        <h2 id="andnode">AndNode</h2>
        <p>The purpose of the AndNode is to perform a logical AND operation on its input ports. When all connected input ports return true, the output result will also be true. If any connected input port returns false, the output result will be false.</p>
    </div>
    

    <div class="section">
        <h2 id="anyinstancepassespredicatenode">AnyInstancePassesPredicateNode</h2>
        <p>The AnyInstancePassesPredicateNode is used to process a list of NounInstances and check if any instance passes a specified 'predicate', which is a ValueVerb. The ValueVerb must have the appropriate inputs and outputs. The node has two output ports, one bool which is true if the predicate evaluates to true on any instance in the list and false otherwise, and another for the first instance if there is one.</p>
    </div>
    

    <div class="section">
        <h2 id="areequalnode">AreEqualNode</h2>
        <p>The AreEqualNode is used to compare two objects for equality. The <a href="/nodes#dynamically_typed">values can be of any type</a>, that type just needs to be chosen using the dropdown menu.</p>
    </div>
    

    <div class="section">
        <h2 id="arithmeticnode">ArithmeticNode</h2>
        <p>The ArithmeticNode is used to perform basic arithmetic operations on two floating-point numbers, such as addition, subtraction, multiplication, and division.</p>
    </div>
    

    <div class="section">
        <h2 id="boolnode">BoolNode</h2>
        <p>The BoolNode is used to create a literal bool value.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodonanytyperunnablenode">CallMethodOnAnyTypeRunnableNode</h2>
        <p>The CallMethodOnAnyTypeRunnableNode can call (almost) any method on any type of object. This flavor of the 'CallMethod' nodes is Runnable, meaning it will execute the method when its turn in the chain comes up. Use this node to use methods that 'set' a value or perform logic.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodonanytypevaluenode">CallMethodOnAnyTypeValueNode</h2>
        <p>The CallMethodOnAnyTypeValueNode can call (almost) any method on any type of object. This flavor of the 'CallMethod' nodes is a ValueNode, meaning the method will execute when any of its output values are requested. Use this node for 'getter' methods. There are other flavors of this node that handle specific types offered for convenience.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodoninstancerunnablenode">CallMethodOnInstanceRunnableNode</h2>
        <p>The CallMethodOnInstanceRunnableNode can call (almost) any method on a given NounInstance. This node is Runnable, meaning it will execute the method when its turn in the chain comes up. Use this node to use methods that 'set' a value or perform logic. There are other flavors of this node that handle specific types offered for convenience.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodoninstancevaluenode">CallMethodOnInstanceValueNode</h2>
        <p>The CallMethodOnInstanceValueNode can call (almost) any method on a given NounInstance. This nodes is a ValueNode, meaning the method will execute when any of its output values are requested. Use this node for 'getter' methods.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodonpropertyrunnablenode">CallMethodOnPropertyRunnableNode</h2>
        <p>The CallMethodOnPropertyRunnableNode can call (almost) any method on a given PropertyInstance. This node is Runnable, meaning it will execute the method when its turn in the chain comes up. Use this node to use methods that 'set' a value or perform logic.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodonpropertyvaluenode">CallMethodOnPropertyValueNode</h2>
        <p>The CallMethodOnPropertyValueNode can call (almost) any method on a given PropertyInstance. This nodes is a ValueNode, meaning the method will execute when any of its output values are requested. Use this node for 'getter' methods.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodonrelationshiprunnablenode">CallMethodOnRelationshipRunnableNode</h2>
        <p>The CallMethodOnRelationshipRunnableNode can call (almost) any method on a given RelationshipInstance. This node is Runnable, meaning it will execute the method when its turn in the chain comes up. Use this node to use methods that 'set' a value or perform logic.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodonrelationshipvaluenode">CallMethodOnRelationshipValueNode</h2>
        <p>The CallMethodOnRelationshipValueNode can call (almost) any method on a given RelationshipInstance. This nodes is a ValueNode, meaning the method will execute when any of its output values are requested. Use this node for 'getter' methods.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodonscriptableobjectrunnablenode">CallMethodOnScriptableObjectRunnableNode</h2>
        <p>The CallMethodOnScriptableObjectRunnableNode can call (almost) any method on a given ScriptableObject. This node is Runnable, meaning it will execute the method when its turn in the chain comes up. Use this node to use methods that 'set' a value or perform logic.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodonscriptableobjectvaluenode">CallMethodOnScriptableObjectValueNode</h2>
        <p>The CallMethodOnScriptableObjectValueNode can call (almost) any method on a given ScriptableObject. This nodes is a ValueNode, meaning the method will execute when any of its output values are requested. Use this node for 'getter' methods.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodonstatrunnablenode">CallMethodOnStatRunnableNode</h2>
        <p>The CallMethodOnStatRunnableNode can call (almost) any method on a given StatInstance. This node is Runnable, meaning it will execute the method when its turn in the chain comes up. Use this node to use methods that 'set' a value or perform logic.</p>
    </div>
    

    <div class="section">
        <h2 id="callmethodonstatvaluenode">CallMethodOnStatValueNode</h2>
        <p>The CallMethodOnStatValueNode can call (almost) any method on a given StatInstance. This nodes is a ValueNode, meaning the method will execute when any of its output values are requested. Use this node for 'getter' methods.</p>
    </div>
    

    <div class="section">
        <h2 id="callstaticmethodrunnablenode">CallStaticMethodRunnableNode</h2>
        <p>The CallStaticMethodRunnableNode can call (almost) any static method. This node is Runnable, meaning it will execute the method when its turn in the chain comes up. Use this node to use methods that 'set' a value or perform logic.</p>
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
        <h2 id="choosefloatnode">ChooseFloatNode</h2>
        <p>The ChooseFloatNode takes in two float values and chooses between them based on a boolean condition, returning the appropriate one.</p>
    </div>
    

    <div class="section">
        <h2 id="chooseintnode">ChooseIntNode</h2>
        <p>The ChooseIntNode takes in two int values and chooses between them based on a boolean condition, returning the appropriate one.</p>
    </div>
    

    <div class="section">
        <h2 id="chooseobjectnode">ChooseObjectNode</h2>
        <p>The ChooseObjectNode takes in two <a href="/nodes#dynamically_typed">values of any type</a> and chooses between them based on a boolean condition, returning the appropriate one.</p>
    </div>
    

    <div class="section">
        <h2 id="chooseprioritizedbranchnode">ChoosePrioritizedBranchNode</h2>
        <p>The ChoosePrioritizedBranchNode can be used to continuously consider conditional logic and run one of several runnable chains based on which one is highest priority. It depends on one or more <a href="#prioritizedbranchnodes">PrioritizedBranchNodes</a> being connected to it, which each have a boolean condition and a chain of RunnableNodes.</p>
        <p>When running, the ChoosePrioritizedBranchNode will run an update after some amount of time (determined by the Refresh Delay value in milliseconds). During this update, each connected PrioritizedBranchNode will be evaluated, from top to bottom. The first one with a condition that evaluates to true will be run. If a branch was already running, and a higher branch becomes true, the running branch is stopped so the new branch can run.</p>
        <p>Additional runnable connections are provided on the ChoosePrioritizedBranchNode which will run under their specific conditions:</p>
        <ul>
            <li>Run Node on all False - the connected node will run if all branches evaluate to false. It is common to simply connect this node back around to to the ChoosePrioritizedBranchNode itself, creating a loop.</li>
            <li>Run Node on Branch Completed - the connected node will run if the currently highest priority branch runs out of nodes to run. It is common to simply connect this node back around to to the ChoosePrioritizedBranchNode itself, creating a loop.</li>
            <li>Run Node on Cancel - the connected node will run if the ChoosePrioritizedBranchNode is interrupted/canceled. This can happen if the ChoosePrioritizedBranchNode is itself on a branch of another ChoosePrioritizedBranchNode. Use this connection to run clean up or stop logic that might not otherwise happen.</li>
        </ul>
    </div>
    

    <div class="section">
        <h2 id="chooserankedweightedactionnode">ChooseRankedWeightedActionNode</h2>
        <p>The ChooseRankedWeightedActionNode is used to select a random action from a list of actions based on their weights, and execute the chosen action in the game flow. The node takes in a NounInstance, which is conceptually the thing taking the action.</p>
        <p>The ChooseRankedWeightedActionNode is an implementation of a Game AI concept we going to call <a href="https://www.gdcvault.com/play/1012410/Improving-AI-Decision-Modeling-Through">Ranked Decision Utility Theory</a>. Each action in the list is a possible action the noun can take. At the time when we choose an action, each one is evaluated and given a 'rank' (int value) and a 'weight' (float value). These values can be static or determined by a ValueVerb. Once all actions have had their rank and weight calculated, one is chosen based on the following steps:</p>
        <ol>
            <li>Actions with a weight of zero are discarded.</li>
            <li>The highest rank among actions is calculated.</li>
            <li>Actions with a rank lower than the highest rank are discarded.</li>
            <li>One action is randomly selected based on each ones weight, giving higher probability to higher weights.</li>
        </ol>
        <p>Each action must have an ActionVerb which is the Effect that that action has when run. The Effect ActionVerb of the chosen action (if there is one) is run.</p>
    </div>
    

    <div class="section">
        <h2 id="choosespritebasedonfloatnode">ChooseSpriteBasedOnFloatNode</h2>
        <p>The ChooseSpriteBasedOnFloatNode can be used to select from a given set of sprites based on a float value. Each sprite is assigned a range (min and max). This node can be used to choose which sprite to display based on a character's stat.</p>
    </div>
    

    <div class="section">
        <h2 id="choosespritebasedonpropertynode">ChooseSpriteBasedOnPropertyNode</h2>
        <p>The ChooseSpriteBasedOnPropertyNode can be used to select from a given set of sprites based on a NounInstance's properties. Each sprite is associated with a property. The first pairing where the given NounInstance has the property is selected and its sprite is returned.</p>
    </div>
    

    <div class="section">
        <h2 id="clampfloatnode">ClampFloatNode</h2>
        <p>The ClampFloatNode is used to limit the value of a float within a specified range, using Mathf.Clamp().</p>
    </div>
    

    <div class="section">
        <h2 id="commentnode">CommentNode</h2>
        <p>The CommentNode is used to add comments or other information to a graph. It does not have inputs or outputs and does not run. It is simply a box where you can add text. It supports resizing.</p>
    </div>
    

    <div class="section">
        <h2 id="comparefloatnode">CompareFloatNode</h2>
        <p>The CompareFloatNode is used to compare two float values and return a boolean result based on the specified comparison type.</p>
    </div>
    

    <div class="section">
        <h2 id="concatstringsnode">ConcatStringsNode</h2>
        <p>The ConcatStringsNode is used to concatenate multiple input strings into a single string output.</p>
    </div>
    

    <div class="section">
        <h2 id="conditionalnode">ConditionalNode</h2>
        <p>The ConditionalNode is used to create a flow-based decision based on a boolean condition. This node has an input port for the condition and two output ports for actions depending on whether the condition is true or false.</p>
    </div>
    

    <div class="section">
        <h2 id="constructobjectnode">ConstructObjectNode</h2>
        <p>The ConstructObjectNode is used to create an object of any given type. If the type has primitive values, this node exposes them for assignment.</p>
    </div>
    

    <div class="section">
        <h2 id="createinstancenode">CreateInstanceNode</h2>
        <p>The CreateInstanceNode is used to create a new instance of a Noun. It can also optionally spawn a new GameObject using a <a href="/saving_loading#spawner">spawner</a>, if provided.</p>
    </div>
    

    <div class="section">
        <h2 id="debuglognode">DebugLogNode</h2>
        <p>The DebugLogNode is used to print the given message using Unity.Debug.Log().</p>
    </div>
    

    <div class="section">
        <h2 id="debuglogobjectnode">DebugLogObjectNode</h2>
        <p>The DebugLogObjectNode is used to log the value of an input object to the console using Unity.Debug.Log().</p>
    </div>
    

    <div class="section">
        <h2 id="destroyinstancenode">DestroyInstanceNode</h2>
        <p>The DestroyInstanceNode is used to destroy a NounInstance, removing it from the list of instances and deleting its associated GameObject.</p>
    </div>
    

    <div class="section">
        <h2 id="exposeobjectnode">ExposeObjectNode</h2>
        <p>The ExposeObjectNode is used to expose an object's properties and fields, allowing you to access their values and use them as inputs for other nodes.</p>
    </div>
    

    <div class="section">
        <h2 id="filterinstancesbypredicatenode">FilterInstancesByPredicateNode</h2>
        <p>The FilterInstancesByPredicateNode is used to filter a list of noun instances in a flow-based based on a predicate. The predicate is a ValueVerb appropriate inputs and outputs. The output is a list of the NounInstances that pass the given predicate, if there are any.</p>
    </div>
    

    <div class="section">
        <h2 id="findchildtransformnode">FindChildTransformNode</h2>
        <p>The FindChildTransformNode is used to find a child transform given a GameObject based on the specified name. It also provides that child's game object and world position for convenience.</p>
    </div>
    

    <div class="section">
        <h2 id="findgameobjectwithnamenode">FindGameObjectWithNameNode</h2>
        <p>The FindGameObjectWithNameNode is used to find and return a GameObject with a specific name in the scene during gameplay.</p>
    </div>
    

    <div class="section">
        <h2 id="findgameobjectwithtagnode">FindGameObjectWithTagNode</h2>
        <p>The FindGameObjectWithTagNode is used to find and return a GameObject with a specific tag in the Unity scene during runtime.</p>
    </div>
    

    <div class="section">
        <h2 id="floatliteralnode">FloatLiteralNode</h2>
        <p>The FloatLiteralNode creates a literal float value.</p>
    </div>
    

    <div class="section">
        <h2 id="floattointnode">FloatToIntNode</h2>
        <p>The FloatToIntNode is used to convert a float value into an integer value. The value is rounded.</p>
    </div>
    

    <div class="section">
        <h2 id="forloopnode">ForLoopNode</h2>
        <p>The ForLoopNode is used to create a 'for loop', executing the connected RunnableNodes a number of times based on the starting and ending values.</p>
    </div>
    

    <div class="section">
        <h2 id="formatstringnode">FormatStringNode</h2>
        <p>The FormatStringNode is used to create a formatted text string. It takes the input text and replaces any placeholders (enclosed in curly braces) with the corresponding values from other nodes connected as inputs based on the input's name. That is, if there is an input with the name 'foo', any occurance of the term '&#123;foo&#125;' in the text value will be replaced with the  value of the foo input.</p>
    </div>
    

    <div class="section">
        <h2 id="gameobjectdistancechecknode">GameObjectDistanceCheckNode</h2>
        <p>The GameObjectDistanceCheckNode is used to compare the distance between two GameObjects, comparing them based on LessThan, GreaterThan, or Approximately.</p>
    </div>
    

    <div class="section">
        <h2 id="getblackboardvariablenode">GetBlackboardVariableNode</h2>
        <p>The GetBlackboardVariableNode is used to retrieve a value from a <a href="/blackboards">Blackboard</a> based on a string key. The type of the value must be specified. The blackboard used is the one attached to the current Verb. To get a blackboard value from a NounInstance, see <a href="#getinstanceblackboardvariablenode">GetInstanceBlackboardVariableNode</a>.</p>
    </div>
    

    <div class="section">
        <h2 id="getcameranode">GetCameraNode</h2>
        <p>The GetCameraNode is used to obtain the camera. Its transform and world position are also provided for convenience.</p>
    </div>
    

    <div class="section">
        <h2 id="getcomponentnode">GetComponentNode</h2>
        <p>The GetComponentNode is used to obtain a component from a given GameObject in Unity, either direct or by including all descendants. The type of the component must be given.</p>
    </div>
    

    <div class="section">
        <h2 id="getflagnode">GetFlagNode</h2>
        <p>The GetFlagNode is used to get the current value of a given <a href="/flags">flag</a>.</p>
    </div>
    

    <div class="section">
        <h2 id="getinstanceblackboardvariablenode">GetInstanceBlackboardVariableNode</h2>
        <p>The GetInstanceFromGameObjectNode is used to retrieve a value from a NounInstance's <a href="/blackboards">Blackboard</a> based on a string key. The type of the value must be specified. To get a blackboard value from the Verb see <a href="#getblackboardvariablenode">GetBlackboardVariableNode</a>. </p>
    </div>
    

    <div class="section">
        <h2 id="getinstancefromgameobjectnode">GetInstanceFromGameObjectNode</h2>
        <p>The GetInstanceFromGameObjectNode is used to retrieve the corresponding NounInstance from a given GameObject (if there is one). In order to get the GameObject from a NounInstance see <a href="#getinstancegameobjectnode">GetInstanceGameObjectNode</a>.</p>
    </div>
    

    <div class="section">
        <h2 id="getinstancegameobjectnode">GetInstanceGameObjectNode</h2>
        <p>The GetInstanceGameObjectNode is used to retrieve the corresponding GameObject from a given NounInstance (if there is one). In order to get the GameObject from a NounInstance see <a href="#getinstancefromgameobjectnode">GetInstanceFromGameObjectNode</a>.</p>
    </div>
    

    <div class="section">
        <h2 id="getinstancenode">GetInstanceNode</h2>
        <p>The GetInstanceNode is used to retrieve the corresponding NounInstance from a given NounScriptableObject. If (for some reason) there are multiple NounInstances created from the NounScriptableObject, only the first one is returned.</p>
    </div>
    

    <div class="section">
        <h2 id="getinstancesnode">GetInstancesNode</h2>
        <p>The GetInstancesNode is used to retrieve all NounInstances and provide them as a list. If there are any elements in the list of 'Must Have Properties' then the NounInstances returned will be limited to those have each have all of the given properties.</p>
    </div>
    

    <div class="section">
        <h2 id="getinstancespritenode">GetInstanceSpriteNode</h2>
        <p>The GetInstanceSpriteNode is used retrieve a Sprite value from a given NounInstance (specifically the instances Blackboard).</p>
    </div>
    

    <div class="section">
        <h2 id="getnextlocationinpathnode">GetNextLocationInPathNode</h2>
        <p>The GetNextLocationInPathNode can be used to traverse a given set of Nouns that are connected by a given relationship, find a path from a starting noun to a destination noun, and return the next step in the path.</p>
    </div>
    

    <div class="section">
        <h2 id="getpropertymodifiernode">GetPropertyModifierNode</h2>
        <p>The GetPropertyModifierNode is used to get the property modifier of a PropertyInstance object based on its type.</p>
    </div>
    

    <div class="section">
        <h2 id="getpropertynode">GetPropertyNode</h2>
        <p>The GetPropertyNode is used to retrieve a property instance from a NounInstances in the Narramancer system.</p>
    </div>
    

    <div class="section">
        <h2 id="getrelationshipnode">GetRelationshipNode</h2>
        <p>The GetRelationshipNode is used to get a relationship between two instances.</p>
    </div>
    

    <div class="section">
        <h2 id="getstatnode">GetStatNode</h2>
        <p>The GetStatNode is used to get a stat from a given NounInstance, providing outputs for whether the noun has that stat (boolean), the number value of the stat (float), and the number value of the stat as a percentage (for convenience, only applicable if the stat has set min and max values).</p>
    </div>
    

    <div class="section">
        <h2 id="gettransformnode">GetTransformNode</h2>
        <p>The GetTransformNode is used to get the Transform of a given GameObject.</p>
    </div>
    

    <div class="section">
        <h2 id="getvariablenode">GetVariableNode</h2>
        <p>The GetVariableNode is used to get the value of a given variable. Variables can come from three scopes: either the Global scope, the Scene scope, or the Verb scope.</p>
        <ul>
            <li>Global variables are defined using the<a href="/narramancer_window"> Narramancer Window</a>.</li>
            <li>Scene variables come from a <a href="/components#narramancer_scene">Narramancer Scene</a> component.</li>
            <li>Verb variables correspond to the current Verb's <a href="/verbs#inputs_outputs">inputs</a>.</li>
        </ul>
        <p>See also the <a href="setvariablenode">SetVariableNode</a>.</p>
    </div>
    

    <div class="section">
        <h2 id="inequalitynode">InequalityNode</h2>
        <p>The InequalityNode performs an inequality comparison between two float values, either ApproximatelyEqualTo, GreaterThan, or LessThan. Notice that GreaterThanOrEqualTo and LessThanOrEqualTo are NOT provided, do to the fact that we're comparing float values.</p>
    </div>
    

    <div class="section">
        <h2 id="intarithmeticnode">IntArithmeticNode</h2>
        <p>The IntArithmeticNode is used to perform arithmetic operations on two integer values, ither addition, subtraction, multiplication, or division.</p>
    </div>
    

    <div class="section">
        <h2 id="intinequalitynode">IntInequalityNode</h2>
        <p>The IntInequalityNode performs an inequality comparison between two int values, either ApproximatelyEqualTo, GreaterThan, GreaterThanOrEqualTo, LessThan, or LessThanOrEqualTo.</p>
    </div>
    

    <div class="section">
        <h2 id="intliteralnode">IntLiteralNode</h2>
        <p>The IntLiteralNode is used to create an integer literal.</p>
    </div>
    

    <div class="section">
        <h2 id="inttofloatnode">IntToFloatNode</h2>
        <p>The IntToFloatNode is used to convert an integer value into a float value.</p>
    </div>
    

    <div class="section">
        <h2 id="isflagraisednode">IsFlagRaisedNode</h2>
        <p>The IsFlagRaisedNode returns true if the given <a href="/flags">flag</a> is raised.</p>
    </div>
    

    <div class="section">
        <h2 id="isnotnullnode">IsNotNullNode</h2>
        <p>The IsNotNullNode is used to check if an object is not null.</p>
    </div>
    

    <div class="section">
        <h2 id="listanynode">ListAnyNode</h2>
        <p>The ListAnyNode returns true if the given list has one or more elements in it. The type of elements must be assigned.</p>
    </div>
    

    <div class="section">
        <h2 id="listaveragenode">ListAverageNode</h2>
        <p>The ListAverageNode is used to calculate the average value of elements within a list. The node takes an input list, processes each element using a predicate (ValueVerb), and calculates the average value of these elements.</p>
    </div>
    

    <div class="section">
        <h2 id="listchooseonenode">ListChooseOneNode</h2>
        <p>The ListChooseOneNode randomly selects a single element from a list. The type of elements must be assigned.</p>
    </div>
    

    <div class="section">
        <h2 id="listcountnode">ListCountNode</h2>
        <p>The ListCountNode is used to count the number of elements in a list. The type of elements must be assigned.</p>
    </div>
    

    <div class="section">
        <h2 id="listfilternode">ListFilterNode</h2>
        <p>The ListFilterNode is used to filter elements in a list based on a predicate. A ValueVerb must be assigned as the predicate with the appropriate inputs and output (one boolean). The resulting list will be all elements from the input list that passed the predicate. The type of elements must be assigned.</p>
    </div>
    

    <div class="section">
        <h2 id="listfirstnode">ListFirstNode</h2>
        <p>The ListFirstNode returns the first element out of the given list.</p>
    </div>
    

    <div class="section">
        <h2 id="listforeachnode">ListForEachNode</h2>
        <p>The ListForEachNode iterates over a given list and runs the connected RunnableNode for each one.</p>
    </div>
    

    <div class="section">
        <h2 id="listordernode">ListOrderNode</h2>
        <p>The ListOrderNode is used to sort a list based on a predicate and returns the sorted list as output.</p>
    </div>
    

    <div class="section">
        <h2 id="listselectnode">ListSelectNode</h2>
        <p>The ListSelectNode is used to <a href="https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.select?view=net-8.0">select</a> or transfrom elements from a a given list based on a predicate.</p>
    </div>
    

    <div class="section">
        <h2 id="listsubtractnode">ListSubtractNode</h2>
        <p>The ListSubtractNode is used to subtract elements from one given list from another list.</p>
    </div>
    

    <div class="section">
        <h2 id="listsumnode">ListSumNode</h2>
        <p>The ListSumNode is used to calculate the sum of a list of elements. The value of each element is determined by the given predicate (ValueVerb).</p>
    </div>
    

    <div class="section">
        <h2 id="listunionnode">ListUnionNode</h2>
        <p>The ListUnionNode performs a union on the two given lists. Additional elements can also be attached individually to the 'elements' port that will also be added to the resulting list. The operation is specifically a union, meaning that each unique element will only appear at most once in the output list.</p>
    </div>
    

    <div class="section">
        <h2 id="loadassetfromresourcesnode">LoadAssetFromResourcesNode</h2>
        <p>The LoadAssetFromResourcesNode is used to load assets from the Unity Resources using a string value path.</p>
    </div>
    

    <div class="section">
        <h2 id="makecolorlistnode">MakeColorListNode</h2>
        <p>The MakeColorListNode is used to create and output a list of colors.</p>
    </div>
    

    <div class="section">
        <h2 id="makelistnode">MakeListNode</h2>
        <p>The MakeListNode is used to create and output a list of ScriptableObjects. The type of the elements in the output list must be assigned (and that type must extend from ScriptableObject).</p>
    </div>
    

    <div class="section">
        <h2 id="mapto2dtablenode">MapTo2DTableNode</h2>
        <p>The MapTo2DTableNode maps two input float values (x and y) to a corresponding float value on a 2D table. The min and max values of the table can be manipulated to create a gradient or vector field.</p>
    </div>
    

    <div class="section">
        <h2 id="maptocurvenode">MapToCurveNode</h2>
        <p>The MapToCurveNode takes an input float value and maps it to an output value using the provided AnimationCurve.</p>
    </div>
    

    <div class="section">
        <h2 id="modifystatnode">ModifyStatNode</h2>
        <p>The ModifyStatNode is used to modify a stat value for a given NounInstance. It allows you to increase, decrease, or set a specific stat's value, with optional constraints.</p>
    </div>
    

    <div class="section">
        <h2 id="multiplyfloatsnode">MultiplyFloatsNode</h2>
        <p>The MultiplyFloatsNode is used to multiply multiple float values together and output the resulting product. Any number of values can be connected to the node's input port.</p>
    </div>
    

    <div class="section">
        <h2 id="notnode">NotNode</h2>
        <p>The NotNode is used to invert the value of its input, returning the 'not' value.</p>
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
        <h2 id="offerobjectsaschoicesnode">OfferObjectsAsChoicesNode</h2>
        <p>The OfferObjectsAsChoicesNode is used to present a list of choices to the player, enabling them to select an object or value from the list. When the player selects a choice, the associated action is executed, and control is passed to the next node in the flow.</p>
    </div>
    

    <div class="section">
        <h2 id="ornode">OrNode</h2>
        <p>The OrNode is used to perform an OR logic operation in a flow-based system for game flow and logic called Narramancer.  Any number of values can be connected to the node's input port and the result is true if any of the inputs are true, or false if all inputs are false.</p>
    </div>
    

    <div class="section">
        <h2 id="outputnode">OutputNode</h2>
        <p>The OutputNode is only applicable to ValueVerbs and is used to assign the verb's <a href="/verbs#inputs_outputs">output values</a>.</p>
    </div>
    

    <div class="section">
        <h2 id="parallelnode">ParallelNode</h2>
        <p>The ParallelNode is used to create parallel execution flow by running all connected RunnableNodes simultaneously.</p>
    </div>
    

    <div class="section">
        <h2 id="playsoundnode">PlaySoundNode</h2>
        <p>The PlaySoundNode is used to play an audio clip using a provided AudioSource or finding one if it's not available.</p>
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


    <div class="section">
        <h2 id="prioritizedbranchnode">PrioritizedBranchNode</h2>
        <p>Used by the <a href="#chooseprioritizedbranchnode">ChoosePrioritizedBranchNode</a>, the PrioritizedBranchNode represents a possible prioritized branch that can be chosen if it's input condition is true.</p>
    </div>
    

    <div class="section">
        <h2 id="raiseflagnode">RaiseFlagNode</h2>
        <p>The RaiseFlagNode is used to raise the given <a href="/flags">flag</a>.</p>
    </div>
    

    <div class="section">
        <h2 id="randomfloatnode">RandomFloatNode</h2>
        <p>The RandomFloatNode generates a random float value within a specified range.</p>
    </div>
    

    <div class="section">
        <h2 id="randomnextnode">RandomNextNode</h2>
        <p>The RandomNextNode randomly selects and runs one of its connected RunnableNodes.</p>
    </div>
    

    <div class="section">
        <h2 id="removeflagnode">RemoveFlagNode</h2>
        <p>The RemoveFlagNode is used to 'remove' a <a href="flags">flag</a>, meaning the flag is no longer raised.</p>
    </div>
    

    <div class="section">
        <h2 id="removepropertiesnode">RemovePropertiesNode</h2>
        <p>The RemovePropertiesNode is used to remove a property or properties from a NounInstance. It accepts a list of PropertyScriptableObject instances, which represent the properties to be removed.</p>
    </div>
    

    <div class="section">
        <h2 id="removerelationshipnode">RemoveRelationshipNode</h2>
        <p>The RemoveRelationshipNode is used to remove relationships between NounInstances.</p>
    </div>
    

    <div class="section">
        <h2 id="rollnode">RollNode</h2>
        <p>The RollNode is used randomly run one of the two connected RunnableNodes. A 'roll' is performed, choosing a random float value between 0.0 and 1.0. If the value is higher than the given threshold than the top chain is taken, otherwise the bottom.</p>
    </div>
    

    <div class="section">
        <h2 id="rootnode">RootNode</h2>
        <p>The RootNode is the starting point for ActionVerbs.</p>
    </div>
    

    <div class="section">
        <h2 id="routenode">RouteNode</h2>
        <p>The RouteNodes are provided for organization. They simply consolidate or reroute RunnableNode connections.</p>
    </div>
    

    <div class="section">
        <h2 id="runactionverbfordurationnode">RunActionVerbForDurationNode</h2>
        <p>The RunActionVerbForDurationNode is similar to RunActionVerbNode, but will cancel/interrupt the ActionVerb after the given duration.</p>
    </div>
    

    <div class="section">
        <h2 id="runactionverbnode">RunActionVerbNode</h2>
        <p>The RunActionVerbNode is used to run an ActionVerb.</p>
    </div>
    

    <div class="section">
        <h2 id="runactionverbwhileconditionistruenode">RunActionVerbWhileConditionIsTrueNode</h2>
        <p>The RunActionVerbForDurationNode is similar to RunActionVerbNode, but only if the given condition evaluates to true and will cancel/interrupt the ActionVerb if the condition becomes false.</p>
    </div>
    
    <div class="section">
        <h2 id="runvalueverbnode">RunValueVerbNode</h2>
        <p>The RunValueVerbNode executes the given ValueVerb.</p>
    </div>
    

    <div class="section">
        <h2 id="selectinstancesbypredicatenode">SelectInstancesByPredicateNode</h2>
        <p>The SelectInstancesByPredicateNode is used to select NounInstances based on a predicate (ValueVerb).</p>
    </div>
    

    <div class="section">
        <h2 id="sequenceofnodesnode">SequenceOfNodesNode</h2>
        <p>The SequenceOfNodesNode allows you to define a series of RunnableNodes that should be executed one after another in the order they are positioned vertically.</p>
    </div>
    

    <div class="section">
        <h2 id="setblackboardvariablenode">SetBlackboardVariableNode</h2>
        <p>The SetBlackboardVariableNode is used to set a variable in the <a href="/blackboards">Blackboard</a> based on a string key.</p>
    </div>
    

    <div class="section">
        <h2 id="setflagnode">SetFlagNode</h2>
        <p>The SetFlagNode set the given <a href="flags">flag</a> to the given value. Setting a flag to 1 or more is the same as 'raising' it, setting it to 0 is the same as 'removing' it.</p>
    </div>
    

    <div class="section">
        <h2 id="setimagespritenode">SetImageSpriteNode</h2>
        <p>The SetImageSpriteNode takes in a Unity.Image and assigns the given sprite to it.</p>
    </div>
    

    <div class="section">
        <h2 id="setinstanceblackboardvariablenode">SetInstanceBlackboardVariableNode</h2>
        <p>The SetInstanceBlackboardVariableNode is used to assign a value to a NounInstance's blackboard.</p>
    </div>
    

    <div class="section">
        <h2 id="setinstancegameobjectnode">SetInstanceGameObjectNode</h2>
        <p>The SetInstanceGameObjectNode is used assign the given GameObject to the given NounInstance, creating a two way connection.</p>
    </div>
    

    <div class="section">
        <h2 id="settextnode">SetTextNode</h2>
        <p>The SetTextNode assigns the text value of a Unity Text component.</p>
    </div>
    

    <div class="section">
        <h2 id="setvariablenode">SetVariableNode</h2>
        <p>The SetVariableNode is used to assign the value of a given variable. Variables can come from three scopes: either the Global scope, the Scene scope, or the Verb scope.</p>
        <ul>
            <li>Global variables are defined using the<a href="/narramancer_window#variables"> Narramancer Window</a>.</li>
            <li>Scene variables come from a <a href="/components#narramancer_scene">Narramancer Scene</a> component.</li>
            <li>Verb variables correspond to the current Verb's <a href="/verbs#inputs_outputs">inputs</a>.</li>
        </ul>
        <p>See also the <a href="getvariablenode">GetVariableNode</a>.</p>
    </div>
    

    <div class="section">
        <h2 id="spawnnode">SpawnNode</h2>
        <p>The SpawnNode is used to spawn a GameObject using a <a href="/components#spawner">SerializedSpawner</a>.</p>
    </div>
    

    <div class="section">
        <h2 id="starttimernode">StartTimerNode</h2>
        <p>The StartTimerNode starts a timer for the given number of seconds. It does not halt, and immediately allows the next RunnableNode to execute. Other nodes can then use the bool outputs of the StartTimerNode to determine if the timer is completed or not.</p>
    </div>
    

    <div class="section">
        <h2 id="stopnoderunnernode">StopNodeRunnerNode</h2>
        <p>The StopNodeRunnerNode is used to stop and reset the execution of a node runner.</p>
    </div>
    

    <div class="section">
        <h2 id="stringliteralnode">StringLiteralNode</h2>
        <p>The StringLiteralNode is used to create a string.</p>
    </div>
    

    <div class="section">
        <h2 id="sumfloatsnode">SumFloatsNode</h2>
        <p>The SumFloatsNode is used to sum multiple float values. Any number of values can be connected to the node's input port.</p>
    </div>
    

    <div class="section">
        <h2 id="switchonintnode">SwitchOnIntNode</h2>
        <p>The SwitchOnIntNode selects a connected RunnableNode based on an input int value.</p>
    </div>
    

    <div class="section">
        <h2 id="tostringnode">ToStringNode</h2>
        <p>The ToStringNode is used to convert any object into a string representation.</p>
    </div>
    

    <div class="section">
        <h2 id="translategameobjectnode">TranslateGameObjectNode</h2>
        <p>The TranslateGameObjectNode is used to translate a GameObject. It allows you to move it by duration, speed, or immediately based on user-defined values. The GameObject MUST have <a href="/saving_loading#serializing_components">SerializableTranform</a> component attached to it.</p>
    </div>
    

    <div class="section">
        <h2 id="tweengameobjectrotationnode">TweenGameObjectRotationNode</h2>
        <p>The TweenGameObjectRotationNode is used to tween the rotation of a GameObject. The GameObject MUST have <a href="/saving_loading#serializing_components">SerializableTranform</a> component attached to it.</p>
    </div>
    

    <div class="section">
        <h2 id="unityobjectnode">UnityObjectNode</h2>
        <p>The UnityObjectNode allows you to reference a UnityObject, such as a ScriptableObject, within a Verb.</p>
    </div>
    

    <div class="section">
        <h2 id="waitnode">WaitNode</h2>
        <p>The WaitNode creates a pause for the given duration.</p>
    </div>
    

    <div class="section">
        <h2 id="waituntilnode">WaitUntilNode</h2>
        <p>The WaitUntilNode waits until a specific condition is met before continuing the execution of other nodes. The refresh delay determines (in milliseconds) how often the condition should be checked for changes. When the condition becomes true, the node will resume the execution of the following nodes in the flow.</p>
    </div>
    
    
<a href="/nouns"><button class="next">Next: Nouns</button></a>