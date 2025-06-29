import os
import json
from typing import List, Dict, Any
from dotenv import load_dotenv  
import os 

# 1. python_guide 폴더 내 html 파일 리스트를 읽어오는 함수
def list_html_files(guide_dir: str) -> List[str]:
    """
    지정한 폴더 내의 모든 .html 파일 경로 리스트를 반환합니다.
    """
    return [
        os.path.join(guide_dir, f)
        for f in os.listdir(guide_dir)
        if f.endswith('.html')
    ]

# 2. 특정 폴더 내 json 파일들을 읽어와 변수에 저장하는 함수
def load_json_files(folder: str) -> Dict[str, Any]:
    """
    폴더 내 모든 .json 파일을 읽어와 {파일명: 데이터} 딕셔너리로 반환합니다.
    """
    data = {}
    for fname in os.listdir(folder):
        if fname.endswith('.json'):
            path = os.path.join(folder, fname)
            with open(path, encoding='utf-8') as f:
                data[fname] = json.load(f)
    return data

# 3. html 파일을 tistory에 업로드하는 함수 (제목, 태그 포함)
def upload_to_tistory(html_path: str, title: str, tags: List[str], access_token: str, blog_name: str) -> Dict[str, Any]:
    """
    Tistory Open API를 사용해 html 파일을 포스트로 업로드합니다.
    - html_path: 업로드할 html 파일 경로
    - title: 포스트 제목
    - tags: 태그 리스트
    - access_token: Tistory API 토큰
    - blog_name: 티스토리 블로그 이름
    반환값: Tistory API 응답(JSON)
    """
    import requests
    with open(html_path, encoding='utf-8') as f:
        content = f.read()
    url = 'https://www.tistory.com/apis/post/write'
    data = {
        'access_token': access_token,
        'output': 'json',
        'blogName': blog_name,
        'title': title,
        'content': content,
        'tag': ','.join(tags),
        'visibility': 3  # 3: 발행
    }
    response = requests.post(url, data=data)
    return response.json()

def get_tistory_categories(access_token: str, blog_name: str, output: str = 'json') -> dict:
    """
    Tistory 블로그의 카테고리 목록을 가져옵니다.
    :param access_token: Tistory API 토큰
    :param blog_name: 블로그 이름
    :param output: 출력 형식 (기본값: 'json')
    :return: 카테고리 목록(JSON)
    """
    import requests
    url = 'https://www.tistory.com/apis/category/list'
    params = {
        'access_token': access_token,
        'output': output,
        'blogName': blog_name
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    access_token = os.getenv("ACCESS_TOKEN")
    blog_name = os.getenv("BLOG_NAME")
    return_value = get_tistory_categories(access_token, blog_name)  # 예시로 카테고리 목록 가져오기
    pass

if __name__ == "__main__":
    # 예시 실행
    guide_dir = 'python_guide'
    html_files = list_html_files(guide_dir)
    print("HTML Files:", html_files)

    json_folder = 'data'
    json_data = load_json_files(json_folder)
    print("JSON Data:", json_data)

    main()


