from aps.models.user import UserAbstract


class User(UserAbstract):
    __tablename__ = "user"
    _email_index_name = "ix_user_email"
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return f'<MyUser {self.name} ({self.email})>'
