from django.db import models


class PropertyInquiry(models.Model):
    # User inputs
    address = models.CharField(max_length=255)
    lot_size_acres = models.DecimalField(max_digits=10, decimal_places=2)
    user_context = models.TextField(blank=True, null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address} ({self.lot_size_acres} acres)"


class PropertyEstimate(models.Model):
    # Link back to the inquiry that triggered this estimate
    inquiry = models.ForeignKey(
        PropertyInquiry, on_delete=models.CASCADE, related_name="estimates"
    )

    # AI-generated fields
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    estimated_net_cash_flow = models.DecimalField(max_digits=15, decimal_places=2)
    estimated_revenue = models.DecimalField(max_digits=15, decimal_places=2)
    estimated_cost = models.DecimalField(max_digits=15, decimal_places=2)

    # Raw AI response for debugging / admin view
    raw_response = models.JSONField()

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Estimate for {self.inquiry.address} on {self.created_at.date()}"
