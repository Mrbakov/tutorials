<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Task extends Model
{
    protected $fillable = [
        'project_id',
        'body',
        'completed'
    ];

    public function project()
    {
        return $this->belongsTo(Project::class);
    }
}
