from odoo import models, fields, api
from datetime import datetime

class ProjectStageTracker(models.Model):
    _inherit = 'project.task'  # Changed from crm.lead to project.task

    last_stage_change = fields.Datetime(string="Last Stage Change", default=fields.Datetime.now)
    days_in_stage = fields.Integer(string="Days in Current Stage", compute='_compute_time_in_stage', store=True)
    hours_in_stage = fields.Integer(string="Hours in Current Stage", compute='_compute_time_in_stage', store=True)
    minutes_in_stage = fields.Integer(string="Minutes in Current Stage", compute='_compute_time_in_stage', store=True)

    @api.depends('last_stage_change')
    def _compute_time_in_stage(self):
        """Compute days, hours, and minutes spent in the current stage."""
        for task in self:
            if task.last_stage_change:
                time_diff = datetime.now() - task.last_stage_change
                task.days_in_stage = time_diff.days
                task.hours_in_stage = time_diff.seconds // 3600
                task.minutes_in_stage = (time_diff.seconds % 3600) // 60
            else:
                task.days_in_stage = 0
                task.hours_in_stage = 0
                task.minutes_in_stage = 0

    def write(self, vals):
        """Override write method to log time spent in each stage when stage_id changes."""
        for task in self:
            old_stage = task.stage_id
            old_stage_date = task.last_stage_change

            if 'stage_id' in vals and vals['stage_id'] != old_stage.id:
                if old_stage_date:
                    time_spent = datetime.now() - old_stage_date
                    days = time_spent.days
                    hours = time_spent.seconds // 3600
                    minutes = (time_spent.seconds % 3600) // 60
                else:
                    days, hours, minutes = 0, 0, 0

                # Log message in chatter
                task.message_post(
                    body=f"Spent {days} days, {hours} hours, and {minutes} minutes in stage: {old_stage.name}"
                )

                # Update last stage change date
                vals['last_stage_change'] = fields.Datetime.now()

        return super(ProjectStageTracker, self).write(vals)
