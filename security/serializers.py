from rest_framework import serializers

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    method = serializers.ChoiceField(choices=[
        ("plain", "Plain Text"),
        ("sha256", "SHA256"),
        ("salted", "SHA256 + Salt"),
        ("bcrypt", "Bcrypt"),
    ])
    
    
class RainbowChallengeSerializer(serializers.Serializer):
    guess = serializers.CharField(required=True)