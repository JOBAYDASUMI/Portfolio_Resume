from django.contrib import admin

from myApp.models import *

admin.site.register(CustomUser)
admin.site.register(ResumeModel)
admin.site.register(LanguageModel)
admin.site.register(IntermediateLanguageModel)
admin.site.register(SkillModel)
admin.site.register(IntermediateSkillModel)
admin.site.register(EducationModel)
admin.site.register(IntermediateEducationModel)
admin.site.register(InterestModel)
admin.site.register(IntermediateInterestModel)
admin.site.register(ExperienceModel)
admin.site.register(IntermediateExperienceModel)



