from rest_framework import serializers
 
from funds.models import Fund
 
class FundSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
 
    class Meta:
        model = Fund
        fields = ('url', 'id', 'created', 'name', 'date', 'user_story', 'user_task', 'content', 'expenses', 'profit', 'user')
        extra_kwargs = {
            'url': {
                'view_name': 'funds:fund-detail',
            }
        }