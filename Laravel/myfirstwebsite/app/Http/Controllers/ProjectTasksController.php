<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Task;
use App\Project;

class ProjectTasksController extends Controller
{
    public function store(Project $project)
    {
        $project -> addTask(request('description'));

        return $project->tasks();
    }

    public function update(Request $request, Task $task)
    {
        $task->update([
            'completed' => request() -> has('completed')
        ]);

        return back;
    }
}
