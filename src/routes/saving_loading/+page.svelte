<div class="section">
    <h2 id="overview">Saving and Loading</h2>
    <p>Saving in Narramancer takes the nouns plus any verbs and serializes them down into a save file, that can then be loaded at a later time. Verbs are built in such a way that even if it is in the middle of running an action, it remembers where it was and what it was doing, and can pick up right where it left off when re-loaded.</p>
</div>

<div class="section">
    <h2 id="serializing_components">Serializing Parts of a Scene</h2>
    <p>In addition to verbs and nouns, you will probably need various aspects of your scene saved. In order to tell Narramancer which GameObjects need to be remembered, you must attach various Narramancer components to them.</p>
    <h4 id="overview">SerializeTransform</h4>
    <p>The SerializeTransform component will save and load all aspects of a GameObject's Transform, including its position and rotation. This component is required to use Translate and Rotate Nodes on a GameObject.</p>
    <h4 id="overview">SerializeImage</h4>
    <p>The SerializeImage component will save and load all aspects of a GameObject's Image, specifically it's sprite and the texture assigned..</p>
    <h4 id="overview">SerializeRectTransform</h4>
    <p>The SerializeRectTransform component will save and load all aspects of a GameObject's RectTransform, including its position and layout values.</p>
    <h4 id="overview">SerializeText</h4>
    <p>The SerializeText component will save and load the text value of a GameObject's Text Component.</p>
    <h4 id="overview">SerializeSpriteRenderer</h4>
    <p>The SerializeSpriteRenderer component will save and load the sprite assigned to a GameObject's SpriteRenderer.</p>
</div>

<div class="section">
    <h2 id="overview">Saving the Relationship Between a Noun and a GameObject</h2>
    <p>If a NounInstance is associated with a GameObject it is highly recommend to add a SerializeNounInstanceReference component to that GameObject in order to maintain that relationship after a load.</p>
</div>

<div class="section">
    <h2 id="overview">SerializableMonoBehaviour</h2>
    <p>If the needs of your game are not met by the above components it is simply a matter of writing a custom component.</p>
    <p>Simply create a new component that either extends from SerializableMonoBehaviour OR implements ISerializableMonoBehaviour.</p>
    <p>If your component extends from SerializableMonoBehaviour, any appropriate fields with the SerializeMonoBehaviourFieldAttribute attached to them will automatically be stored on save and assigned on load. In more complex cases, you may need to override either or both Serialize() and Deserialize() and perform additional logic by assessing the StoryInstance (just be sure to call the base.Serialize() and base.Deserialize()).</p>
</div>


<a href="/components"><button class="next">Next: Components</button></a>