from rest_framework import serializers

from .models import Task, Step


class StepSerializer(serializers.ModelSerializer):
    completed = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Step
        fields = ['note', 'attachment', 'deadline', 'completed', 'created_at',]


class TaskSerializer(serializers.ModelSerializer):
    completed = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    steps = StepSerializer(many=True)

    class Meta:
        model = Task
        fields = ['title', 'completed', 'created_at', 'deadline', 'user', 'steps',]

    def create(self, validated_data):
        steps_data = validated_data.pop('steps')
        task = Task.objects.create(**validated_data)

        for step_data in steps_data:
            Step.objects.create(task=task, **step_data)

        return task
    
    def update(self, instance, validated_data):
        steps_data = validated_data.pop('steps')
        instance.title = validated_data.get('title', instance.title)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.save()

        for step_data in steps_data:
            step = instance.steps.get(id=step_data.get('id', None))
            step.note = step_data.get('note', step.note)
            step.deadline = step_data.get('deadline', step.deadline)
            step.save()

        return instance
