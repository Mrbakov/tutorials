<!DOCTYPE html>
<html>
    <head>
    <body>
    <h1>Create project</h1>

    <form method="POST" action="/projects">
    {{ csrf_field() }}
    
        <div>
            <input type="text" name="title" placeholder="Project title">
        </div>

        <div>
            <input type="text" name="description" placeholder="Project description">
        </div>

        <div>
            <button type="submit">Crate Project</button>
        </div>

    </form>
    </body>
</html>