#version 150

#moj_import <fog.glsl>

in vec3 Position;
in vec4 Color;
in vec2 UV0;
in ivec2 UV2;

uniform sampler2D Sampler2;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;
uniform int FogShape;

out float vertexDistance;
out vec4 vertexColor;
out vec2 texCoord0;

void main() {
	ivec3 control = ivec3(0);
	if (Position.y > 400.0) control = ivec3(Color.rgb * 255.0 + 0.5);
	if (control == ivec3(1, 0, 0)) {
		gl_Position = ProjMat * ModelViewMat * vec4(Position + vec3(0.0, -800.0, 0.0), 1.0);
		gl_Position.xy += vec2(-1.0, 0.0);
		vertexColor = vec4(1.0);
	}
	else if (control == ivec3(2, 0, 0)) {
		gl_Position = ProjMat * ModelViewMat * vec4(Position + vec3(-80.0, -800.0, 0.0), 1.0);
		gl_Position.xy += vec2(0.0, 0.0);
		vertexColor = vec4(1.0);
	}
	else if (control == ivec3(3, 0, 0)) {
		gl_Position = ProjMat * ModelViewMat * vec4(Position + vec3(-160.0, -800.0, 0.0), 1.0);
		gl_Position.xy += vec2(1.0, 0.0);
		vertexColor = vec4(1.0);
	}
	else if (control == ivec3(0, 1, 0)) {
		gl_Position = ProjMat * ModelViewMat * vec4(Position + vec3(0.0, -880.0, 0.0), 1.0);
		gl_Position.xy += vec2(-1.0, -1.0);
		vertexColor = vec4(1.0);
	}
	else if (control == ivec3(0, 2, 0)) {
		gl_Position = ProjMat * ModelViewMat * vec4(Position + vec3(-80.0, -880.0, 0.0), 1.0);
		gl_Position.xy += vec2(0.0, -1.0);
		vertexColor = vec4(1.0);
	}
	else if (control == ivec3(0, 3, 0)) {
		gl_Position = ProjMat * ModelViewMat * vec4(Position + vec3(-160.0, -880.0, 0.0), 1.0);
		gl_Position.xy += vec2(1.0, -1.0);
		vertexColor = vec4(1.0);
	}
	else if (control == ivec3(0, 0, 1)) {
		gl_Position = ProjMat * ModelViewMat * vec4(Position + vec3(0.0, -960.0, 0.0), 1.0);
		gl_Position.xy += vec2(-1.0, -2.0);
		vertexColor = vec4(1.0);
	}
	else if (control == ivec3(0, 0, 2)) {
		gl_Position = ProjMat * ModelViewMat * vec4(Position + vec3(-80.0, -960.0, 0.0), 1.0);
		gl_Position.xy += vec2(0.0, -2.0);
		vertexColor = vec4(1.0);
	}
	else if (control == ivec3(0, 0, 3)) {
		gl_Position = ProjMat * ModelViewMat * vec4(Position + vec3(-160.0, -960.0, 0.0), 1.0);
		gl_Position.xy += vec2(1.0, -2.0);
		vertexColor = vec4(1.0);
	}
	else {
		gl_Position = ProjMat * ModelViewMat * vec4(Position, 1.0);
		vertexColor = Color * texelFetch(Sampler2, UV2 / 16, 0);
	}
	vertexDistance = fog_distance(Position, FogShape);
	texCoord0 = UV0;
}
