from rest_framework import serializers
from my_app.models import User, Client


class UserSeralizers(serializers.ModelSerializer):
	class Meta:
		model = User
		# fields = '__all__' #qilib yozishimiz ham mumkin bunda hamma fieldlarni chiqarib beradi
		fields = ('id', 'firstname', 'lastname', 'username',
		          'username')  # bu kurinishdagi esa faqat biz xoxlaganlarini chiqarib beradi


class ClientSeralizers(serializers.ModelSerializer):
	class Meta:
		model = Client
		# fields = '__all__' #qilib yozishimiz ham mumkin bunda hamma fieldlarni chiqarib beradi
		fields = ('id', 'FirstName', 'LastName', 'CarModel', 'CarNumber', 'PhoneNumber',
		          'CreatedUserld')  # bu kurinishdagi esa faqat biz xoxlaganlarini chiqarib beradi


class UserREGSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			"id",
			'firstname',
			'lastname',
			'username',
			'password']
		extra_kwargs = {
			'password': {'write_only': True}
		}

	def create(self, validated_data):
		auth_user = User.objects.create_user(**validated_data)
		return auth_user
