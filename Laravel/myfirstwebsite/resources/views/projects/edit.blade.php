@extends('layout')

@section('content')

<h1>Edit project</h1>

<form method="POST" action="/project/{{ $project -> id }}">
@method('PATCH')
@csrf

    <div>
        <input
            type="text"
            name="title"
            placeholder="Project title"
            value="{{ $project->title }}"
        />
    </div>

    <div>
        <input
            type="text"
            name="description"
            placeholder="Project description"
            value="{{ $project->description }}"
        />
    </div>

    <div>
        <button type="submit">Submit Project</button>
    </div>
</form>

<form method="POST" action="/project/{{ $project -> id }}">
@method('DELETE')
@csrf
<button type="submit">DELETE</button>
</form>

@endsection
