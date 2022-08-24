text = 'width: 100%; height: 100%; background-image: url("https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyMjA4MTVfODcg%2FMDAxNjYwNTQwNzk1MzIy.u036elV8xL7xTeoYRQSFmkBW_ExnAFjtVRVk26DFpEgg.StnMLAb1lIEFc-6A7kHEdNSBAUuvCuCpRReXd9UhWOog.JPEG%2Fupload_3e9749d181bd3e4d1aa0ac6ac0d38195.jpg")'

import re
matches = re.findall('"(http.*?)"', text)
print(matches[0])