
<div class="section">
  <h2 id="overview">Overview</h2>
  <p>Narramancer is a node-based scripting system with a saving and loading the game state built-in.</p>
  <p>It can be used for branching conversations, as an npc behavior tree, or it can handle the over-all game loop logic.</p>
</div>

<div class="section">
  <h2 id="background">Background</h2>
  <p>The main motivation behind Narramancer is to provide a Unity extension that can chain units of game logic into complex sequences <strong>and</strong> be able to save and load the running sequence at any given time.</p>
  <p>What do we mean by a unit of game logic? For a simple Visual Novel game, the typical units of game logic are:</p>
  <ol>
    <li>
      Show or Hide Graphics, such as characters or backgrounds.
    </li>
    <li>
      Play a sound effect or music.
    </li>
    <li>
      Reveal text to the player, either narrative or character dialog. Wait for the player to confirm.
    </li>
    <li>
      Present the player with two or more choices as selectable buttons. Wait for the player to choose one.
    </li>
  </ol>
  <p>A unit of game logic can be something simple that happens instantatiously or something complex that happens over realtime.</p>
  <p>Narramancer calls these units Nodes (more specifically a RunnableNodes) and has dozens of different Nodes for all kinds of purposes.</p>
  <p></p>
</div>

<div class="section">
  <h2 id="why">Why Narramancer?</h2>
  <p>There are several options when it comes to scripting systems and/or saving solutions. Why should you use Narramancer?</p>
  <table>
    <tr>
      <th>Asset or Package</th>
      <th>Disadvantage(s)</th>
    </tr>
    <tr>
      <td>Unity</td>
      <td>In order to perform the chain(s) actions we are interested in with base Unity it would usually require manually creating Singletons or various inter-dependent scripts.</td>
    </tr>
    <tr>
      <td><a href="https://unity.com/features/unity-visual-scripting">Unity Visual Scripting</a></td>
      <td>Unity Visual Scripting is a powerful scripting system that uses nodes <strong>but</strong> does not provide anyway of serializing what node is running.</td>
    </tr>
    <tr>
      <td><a href="https://fungusgames.com/">Fungus</a></td>
      <td>Fungus is another Unity extension that allows scripting using either flow charts or the Lua language <strong>but</strong> also does not provide anyway of saving and loading.</td>
    </tr>
    <tr>
      <td><a href="https://naninovel.com/">Naninovel</a></td>
      <td>Naninovel is a powerful visual novel engine that <strong>does</strong> have saving and loading built-in, but requires the use of Nani scripts (Document and text based files using a proprietary scripting language).</td>
    </tr>
  </table>
  <br/>
  <p>(To be honest, if you are making a visual novel game and would prefer text-based scripting over node-based then we recommend using Naninovel. It is a feature-rich engine with years of experience and support.)</p>
</div>

<div class="section">
  <h2 id="advantages">Advantages</h2>
  <p>Building a game with the Narramancer system as the 'spine' has two main advantages:</p>
  <ol>
    <li>
      Allowing the player to save and load your game at (almost) any given time is baked in from the start, instead of tacked on later.
    </li>
    <li>
      The flow and overall logic of your game is easy to develop, edit, and visualize.
    </li>
  </ol>
  <br/>
  <p>Narramancer additionally provides other features:</p>
  <ul>
    <li>
      Provides a <a href="/nouns">Table of "Things"</a>; a database of people, places, or items that your game can access and manipulate.
    </li>
    <li>
      ScriptableObject focused: the main classes in Narramancer are built on top of Unity's ScriptableObject, <a href="https://unity.com/how-to/architect-game-code-scriptable-objects">giving the system ease-of-use and modularity</a>.
    </li>
    <li>
      Scene Independent
    </li>
    <li>
      General-Purpose variables
    </li>
    <li>
      Little or no coding required.
    </li>
    <li>
      Rapidly develop and test ideas and logic without having to recompile or even leave play-mode.
    </li>
  </ul>
  
</div>


<a href="/getting_started"><button class="next">Next: Getting Started</button></a>
