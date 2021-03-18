class Meta:
    def __init__(self, *args, **kwargs):
        pass

    def to_dict(self):
        res = {}
        res.update(self.__dict__)
        return res


class Cate(Meta):
    def __init__(self, cate_id=None, cate_name=None, parent_id=None, *args, **kwargs):
        self.cate_id = cate_id
        self.cate_name = cate_name
        self.parent_id = parent_id
        super(Cate, self).__init__(*args, **kwargs)


class Page(Meta):
    def __init__(self, page_id=None, title=None, description=None, *args, **kwargs):
        self.page_id = page_id
        self.title = title
        self.description = description
        super(Page, self).__init__(*args, **kwargs)
