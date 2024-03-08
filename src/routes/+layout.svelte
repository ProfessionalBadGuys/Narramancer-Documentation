

<script>
    import Toc from 'svelte-toc'

    import { Navbar, NavbarBrand, NavItem, NavLink, Container, Row, Col } from '@sveltestrap/sveltestrap';

</script>

<div class="bodybackground">

    <div class="navbar">
        <Navbar color="dark" fixed="top" dark=true>
            <NavbarBrand  href="/">Narramancer</NavbarBrand >
            <NavLink href="https://assetstore.unity.com/packages/tools/behavior-ai/narramancer-269301">Asset Store</NavLink>
            <NavLink href="https://www.youtube.com/@ProfessionalBadGuys/videos">Video Tutorials</NavLink>
            <NavLink href="https://discord.gg/CKqJXfJVzQ">Discord</NavLink>
        </Navbar>
    </div>



    <div class="maincontainer">
        <Container fluid>
            <Row cols=12>
                <Col xs="2">
                    <div class="sidecolumn pt-2">
                        <div class="pt-5"></div>
                        <div class="sidecolumninner">
                            <a href="/">Introduction</a>
                            <a href="/getting_started">Getting Started</a>
                            <a href="/verbs">Verbs</a>
                            <a href="/verb_editor">Verb Editor</a>
                            <a href="/nodes">Nodes</a>
                            <a href="/list_nodes">List of All Nodes</a>
                            <a href="/nouns">Nouns</a>
                            <a href="/narramancer_window">Narramancer Window</a>
                            <a href="/saving_loading">Saving and Loading</a>
                            <a href="/components">Components</a>
                            <a href="/flags">Flags</a>
                        </div>
                    </div>
                </Col>
        
                <Col xs="7">
                    <main>
                        <slot></slot>
                    </main>
                </Col>
        
                <Col xs="3">
                    <div class="sidecolumn">
                        <div class="sidecolumninner">
                            <Toc headingSelector="main :where(h2, h3)" />
                        </div>
                    </div>
                </Col>
            </Row>
        </Container>
    </div>
</div>