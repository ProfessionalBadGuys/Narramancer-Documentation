
<script>
    import Toc from 'svelte-toc'

    import { Navbar, Container, Row, Col } from '@sveltestrap/sveltestrap';

</script>

<div class="bodybackground">

    <div class="navbar">
        <Navbar color="dark" fixed="top">
            Narramancer
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
                            <a href="/list_nodes">Nouns</a>
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